from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.analyze import router as analyze_router

app = FastAPI(
    title="AI Resume Intelligence Analyzer",
    description="AI-powered resume and job description analysis API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-resume-intelligence-analyzer.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "AI Resume Intelligence Analyzer API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
