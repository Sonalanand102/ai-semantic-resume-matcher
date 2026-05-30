from sqlalchemy import Column, Integer, Text
from pgvector.sqlalchemy import Vector

from app.db.base import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(Text, nullable=False)

    job_title = Column(Text, nullable=False)

    location = Column(Text)

    openings = Column(Integer)

    experience_level = Column(Text)

    employment_type = Column(Text)

    job_description = Column(Text, nullable=False)

    search_text = Column(Text, nullable=False)

    embedding = Column(Vector(3072))