import json
import re
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
                "Add GEMINI_API_KEY to environment variables and restart the server."
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
        model="gemini-1.5-flash",  # Updated to supported Gemini model string
        contents=prompt,
    )

    text = response.text.strip()

    # Safely extract JSON content even if wrapped in markdown code blocks
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        text = json_match.group(0)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "recommendations": ["Failed to parse AI response. Please try again."],
            "summary": "Parsing error occurred while processing resume."
        }