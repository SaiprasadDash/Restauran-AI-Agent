from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.app_name,
        "environment": settings.environment,
    }