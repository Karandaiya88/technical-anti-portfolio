"""
Public, read-only profile page data — /u/{username}
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, Postmortem
from app.schemas import PostmortemOut, UserOut

router = APIRouter(prefix="/u", tags=["profile"])


@router.get("/{username}")
def get_public_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    postmortems = (
        db.query(Postmortem)
        .filter(Postmortem.user_id == user.id, Postmortem.is_public.is_(True))
        .order_by(Postmortem.created_at.desc())
        .all()
    )
    return {
        "user": UserOut.model_validate(user),
        "postmortems": [PostmortemOut.model_validate(p) for p in postmortems],
    }
