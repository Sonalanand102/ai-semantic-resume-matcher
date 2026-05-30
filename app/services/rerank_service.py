import google.generativeai as genai

from app.utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def rerank_jobs(
    resume_text: str,
    jobs: list
):

    reranked_results = []

    model = genai.GenerativeModel(
        "gemini-3-flash-preview"
    )

    for job in jobs:

        prompt = f"""
        You are an AI recruiter.

        Compare the resume and job description.

        Give a relevance score between 0 to 100.

        Resume:
        {resume_text}

        Job Title:
        {job['job_title']}

        Job Description:
        {job['job_description']}

        Return ONLY the number.
        """

        response = model.generate_content(
            prompt
        )

        try:

            score = float(
                response.text.strip()
            )

        except:

            score = 0

        job["rerank_score"] = score

        reranked_results.append(job)

    reranked_results.sort(
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked_results[:5]