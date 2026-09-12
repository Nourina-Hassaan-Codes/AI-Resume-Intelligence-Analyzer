import json

from google import genai

from app.core.config import GEMINI_API_KEY


def analyze_resume(
    resume_text: str,
    job_description: str
):
    if not GEMINI_API_KEY:
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "recommendations": [
                "Add GEMINI_API_KEY to backend/.env and restart the server."
            ],
            "summary": "AI analysis is not configured yet."
        }

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are an enterprise recruitment intelligence assistant.

Analyze the candidate resume against the target job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON using this exact structure:

{{
  "match_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "recommendations": [],
  "summary": ""
}}

Rules:
- match_score must be an integer from 0 to 100.
- matching_skills must contain skills found in both the resume and job requirements.
- missing_skills must contain important skills required by the job but not clearly demonstrated in the resume.
- recommendations must contain practical improvement actions.
- summary must briefly explain the candidate's overall fit.
- Do not invent experience.
"""

    response = client.models.generate_content(
       model="gemini-3.6-flash",
        contents=prompt,
    )

    text = response.text.strip()

    if text.startswith("`"):
        text = text.replace("`json", "")
        text = text.replace("`", "")
        text = text.strip()

    return json.loads(text)
