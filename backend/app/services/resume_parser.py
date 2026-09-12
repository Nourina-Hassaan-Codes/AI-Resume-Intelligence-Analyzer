from io import BytesIO
from pathlib import Path

from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document


async def extract_resume_text(file: UploadFile) -> str:
    content = await file.read()

    filename = file.filename.lower()
    extension = Path(filename).suffix

    if extension == ".pdf":
        reader = PdfReader(BytesIO(content))

        pages = []

        for page in reader.pages:
            text = page.extract_text() or ""
            pages.append(text)

        return "\n".join(pages)

    if extension == ".docx":
        document = Document(BytesIO(content))

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)

    if extension == ".txt":
        return content.decode("utf-8", errors="ignore")

    raise ValueError(
        "Unsupported file type. Please upload PDF, DOCX, or TXT."
    )
