from sqlalchemy.orm import Session

from app.models.job import Job

from app.schemas.job_schema import JobCreate

from app.services.embedding_service import generate_embedding


def process_job_ingestion(
    db: Session,
    job_data: JobCreate
):

    embedding_text = f"""
    Job Title: {job_data.job_title}

    Description:
    {job_data.job_description}
    """

    embedding = generate_embedding(
        embedding_text
    )

    new_job = Job(
        company_name=job_data.company_name,

        job_title=job_data.job_title,

        location=job_data.location,

        openings=job_data.openings,

        experience_level=job_data.experience_level,

        employment_type=job_data.employment_type,

        job_description=job_data.job_description,

        search_text=f"""
        {job_data.job_title}
        {job_data.job_description}
        """,

        embedding=embedding
    )

    db.add(new_job)

    db.commit()

    db.refresh(new_job)

    print(
        f"Job processed: {job_data.job_title}"
    )