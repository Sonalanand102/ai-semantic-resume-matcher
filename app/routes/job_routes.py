from fastapi import (
    APIRouter,
    Depends,
    BackgroundTasks
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.job_schema import JobCreate

from app.services.job_service import (
    process_job_ingestion
)

router = APIRouter()


@router.post("/jobs")
def add_job(
    job: JobCreate,

    background_tasks: BackgroundTasks,

    db: Session = Depends(get_db)
):

    background_tasks.add_task(
        process_job_ingestion,
        db,
        job
    )

    return {
        "message": "Job ingestion started"
    }