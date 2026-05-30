from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import text

from app.services.embedding_service import generate_embedding
from app.services.rerank_service import rerank_jobs

def match_resume(
    db: Session,
    resume_text: str,

    location: Optional[str] = None,

    experience_level: Optional[str] = None,

    employment_type: Optional[str] = None
):

    resume_embedding = generate_embedding(resume_text)

    query_text = resume_text

    base_query = """
        SELECT
            id,
            company_name,
            job_title,
            location,
            openings,
            experience_level,
            employment_type,
            job_description,

            embedding <-> :resume_embedding AS semantic_distance,

            ts_rank(
                to_tsvector(search_text),
                plainto_tsquery(:query_text)
            ) AS keyword_rank

        FROM jobs

        WHERE 1=1
    """

    params = {
        "resume_embedding": str(resume_embedding),
        "query_text": query_text
    }

    if location:
        base_query += " AND location = :location"
        params["location"] = location

    if experience_level:
        base_query += " AND experience_level = :experience_level"
        params["experience_level"] = experience_level

    if employment_type:
        base_query += " AND employment_type = :employment_type"
        params["employment_type"] = employment_type

    base_query += """
        ORDER BY
            (
                (1 - (embedding <-> :resume_embedding)) * 0.7
                +
                ts_rank(
                    to_tsvector(search_text),
                    plainto_tsquery(:query_text)
                ) * 0.3
            ) DESC

        LIMIT 20
    """

    query = text(base_query)

    results = db.execute(query, params)

    rows = results.mappings().all()

    formatted_results = []

    for row in rows:

        semantic_score = (
            1 - row["semantic_distance"]
        ) * 100

        formatted_results.append({
            "id": row["id"],
            "company_name": row["company_name"],
            "job_title": row["job_title"],
            "location": row["location"],
            "experience_level": row["experience_level"],
            "employment_type": row["employment_type"],
            "job_description": row["job_description"],
            "semantic_score": round(semantic_score, 2),
            "keyword_rank": round(row["keyword_rank"], 2)
        })

    reranked_results = rerank_jobs(
        resume_text,
        formatted_results
    )

    return reranked_results