from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    company_name: str
    job_title: str
    location: Optional[str] = None
    openings: Optional[int] = None
    experience_level: Optional[str] = None
    employment_type: Optional[str] = None
    job_description: str


class JobResponse(BaseModel):
    id: int
    company_name: str
    job_title: str
    location: Optional[str]
    openings: Optional[int]
    experience_level: Optional[str]
    employment_type: Optional[str]
    job_description: str

    class Config:
        from_attributes = True