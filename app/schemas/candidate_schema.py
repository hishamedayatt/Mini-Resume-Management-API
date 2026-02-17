from pydantic import BaseModel
from datetime import date
from typing import List

class CandidateResponse(BaseModel):
    id: str
    full_name: str
    dob: date
    contact_number: str
    contact_address: str
    education: str
    graduation_year: int
    years_experience: int
    skills: List[str]
    resume_filename: str
