from typing import Optional

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    Query
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.pdf_service import extract_text_from_pdf

from app.services.matching_service import match_resume

router = APIRouter()


@router.post("/match-resume")
async def match_resume_api(
    file: UploadFile = File(...),

    location: Optional[str] = Query(None),

    experience_level: Optional[str] = Query(None),

    employment_type: Optional[str] = Query(None),

    db: Session = Depends(get_db)
):

    resume_text = extract_text_from_pdf(file.file)

    matches = match_resume(
        db=db,
        resume_text=resume_text,
        location=location,
        experience_level=experience_level,
        employment_type=employment_type
    )

    return {
        "matches": matches
    }