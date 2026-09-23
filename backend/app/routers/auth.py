"""
GitHub OAuth login flow.
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from jose import jwt
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.github_client import GitHubClient
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/github/login")
def github_login():
    """Redirects the user to GitHub's OAuth consent screen."""
    url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={settings.github_client_id}"
        f"&redirect_uri={settings.github_callback_url}"
        "&scope=repo read:user user:email"
    )
    return RedirectResponse(url)


@router.get("/github/callback")
async def github_callback(code: str, db: Session = Depends(get_db)):
    """
    Exchanges the OAuth code for a token, fetches the GitHub profile,
    upserts the local user record, and returns a session JWT.
    """
    # Token exchange needs an unauthenticated client for this one call
    client = GitHubClient(access_token="")
    token_data = await client.exchange_code_for_token(
        code=code,
        client_id=settings.github_client_id,
        client_secret=settings.github_client_secret,
        redirect_uri=settings.github_callback_url,
    )
    access_token = token_data.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="GitHub token exchange failed")

    gh = GitHubClient(access_token=access_token)
    profile = await gh.get_authenticated_user()

    user = db.query(User).filter(User.github_id == str(profile["id"])).first()
    if not user:
        user = User(
            github_id=str(profile["id"]),
            username=profile["login"],
            email=profile.get("email"),
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    session_token = jwt.encode(
        {"sub": str(user.id), "github_token": access_token},
        settings.secret_key,
        algorithm="HS256",
    )
    return RedirectResponse(f"{settings.frontend_url}/dashboard?token={session_token}")
