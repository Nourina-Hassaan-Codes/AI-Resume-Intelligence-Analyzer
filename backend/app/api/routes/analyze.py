from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.resume_parser import extract_resume_text
from app.services.ai_analyzer import analyze_resume

router = APIRouter()


@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    if not resume.filename:
        raise HTTPException(
            status_code=400,
            detail="Resume file is required."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description is required."
        )

    try:
        resume_text = await extract_resume_text(resume)

        if not resume_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the resume."
            )

        result = analyze_resume(
            resume_text=resume_text,
            job_description=job_description
        )

        return result

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
