"""
The Technical Anti-Portfolio — FastAPI backend entrypoint.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import Base, engine
from app.routers import auth, repos, postmortems, tags, profile

app = FastAPI(
    title="The Technical Anti-Portfolio API",
    description="Root Cause Analysis & Post-Mortem platform backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(repos.router)
app.include_router(postmortems.router)
app.include_router(tags.router)
app.include_router(profile.router)


@app.on_event("startup")
def on_startup():
    # For local dev convenience. In production, use Alembic migrations instead.
    Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "technical-anti-portfolio-api"}
