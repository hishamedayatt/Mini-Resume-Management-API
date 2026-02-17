from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from typing import Optional
from uuid import uuid4
from datetime import date

from app.storage.candidate_storage import candidates
from app.schemas.candidate_schema import CandidateResponse

router = APIRouter(prefix="/candidates", tags=["Candidates"])


# Upload Candidate
@router.post("", status_code=status.HTTP_201_CREATED)
async def upload_candidate(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    years_experience: int = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...)
):
    allowed_types = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if resume.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOC, DOCX files are allowed"
        )

    candidate_id = str(uuid4())
    skill_list = [skill.strip() for skill in skills.split(",")]

    candidate = {
        "id": candidate_id,
        "full_name": full_name,
        "dob": dob,
        "contact_number": contact_number,
        "contact_address": contact_address,
        "education": education,
        "graduation_year": graduation_year,
        "years_experience": years_experience,
        "skills": skill_list,
        "resume_filename": resume.filename
    }

    candidates.append(candidate)

    return {
        "message": "Candidate uploaded successfully",
        "candidate_id": candidate_id
    }


# List Candidates
@router.get("", response_model=list[CandidateResponse],status_code=200)
def list_candidates(
    skill: Optional[str] = None,
    min_experience: Optional[int] = None,
    graduation_year: Optional[int] = None
):
    results = candidates

    if skill:
        results = [
            c for c in results
            if skill.lower() in [s.lower() for s in c["skills"]]
        ]

    if min_experience is not None:
        results = [
            c for c in results
            if c["years_experience"] >= min_experience
        ]

    if graduation_year is not None:
        results = [
            c for c in results
            if c["graduation_year"] == graduation_year
        ]

    return results


# Get Candidate by ID
@router.get("/{candidate_id}", response_model=CandidateResponse,status_code=200)
def get_candidate(candidate_id: str):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate

    raise HTTPException(status_code=404, detail="Candidate not found")


# Delete Candidate
@router.delete("/{candidate_id}",status_code=200)
def delete_candidate(candidate_id: str):
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            candidates.remove(candidate)
            return {"message": "Candidate deleted successfully"}

    raise HTTPException(status_code=404, detail="Candidate not found")
