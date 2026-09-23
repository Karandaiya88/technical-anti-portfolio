"""
Shared FastAPI dependencies — current user extraction from session JWT.
"""
from fastapi import Depends, Header, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import User


def get_current_user_and_token(
    authorization: str = Header(...), db: Session = Depends(get_db)
) -> tuple[User, str]:
    """
    Expects `Authorization: Bearer <session_jwt>`.
    Returns (User, github_access_token).
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing bearer token")
    token = authorization.removeprefix("Bearer ").strip()

    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    user = db.query(User).filter(User.id == payload["sub"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user, payload["github_token"]
