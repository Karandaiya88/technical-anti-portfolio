"""
Postmortem CRUD — the core content type of the platform.
"""
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user_and_token
from app.models import Postmortem, DiffSnippet, TaxonomyTag
from app.schemas import PostmortemCreate, PostmortemUpdate, PostmortemOut
from app.utils.sanitize import sanitize_code_chunk

router = APIRouter(prefix="/postmortems", tags=["postmortems"])


def _get_or_create_tags(db: Session, tag_names: list[str]) -> list[TaxonomyTag]:
    tags = []
    for name in tag_names:
        tag = db.query(TaxonomyTag).filter(TaxonomyTag.name == name).first()
        if not tag:
            tag = TaxonomyTag(name=name)
            db.add(tag)
            db.flush()
        tags.append(tag)
    return tags


@router.post("", response_model=PostmortemOut)
def create_postmortem(
    payload: PostmortemCreate,
    db: Session = Depends(get_db),
    user_and_token=Depends(get_current_user_and_token),
):
    user, _ = user_and_token
    postmortem = Postmortem(
        user_id=user.id,
        title=payload.title,
        hypothesis=payload.hypothesis,
        breaking_point=payload.breaking_point,
        architectural_rule=payload.architectural_rule,
        is_public=payload.is_public,
        tags=_get_or_create_tags(db, payload.tags),
    )
    for snippet in payload.diff_snippets:
        postmortem.diff_snippets.append(
            DiffSnippet(
                file_path=snippet.file_path,
                faulty_chunk=sanitize_code_chunk(snippet.faulty_chunk),
                resolved_chunk=sanitize_code_chunk(snippet.resolved_chunk),
            )
        )
    db.add(postmortem)
    db.commit()
    db.refresh(postmortem)
    return postmortem


@router.get("/{postmortem_id}", response_model=PostmortemOut)
def get_postmortem(postmortem_id: uuid.UUID, db: Session = Depends(get_db)):
    postmortem = db.query(Postmortem).filter(Postmortem.id == postmortem_id).first()
    if not postmortem:
        raise HTTPException(status_code=404, detail="Postmortem not found")
    return postmortem


@router.get("", response_model=list[PostmortemOut])
def list_postmortems(tag: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Postmortem).filter(Postmortem.is_public.is_(True))
    if tag:
        query = query.join(Postmortem.tags).filter(TaxonomyTag.name == tag)
    return query.order_by(Postmortem.created_at.desc()).all()


@router.put("/{postmortem_id}", response_model=PostmortemOut)
def update_postmortem(
    postmortem_id: uuid.UUID,
    payload: PostmortemUpdate,
    db: Session = Depends(get_db),
    user_and_token=Depends(get_current_user_and_token),
):
    user, _ = user_and_token
    postmortem = db.query(Postmortem).filter(Postmortem.id == postmortem_id).first()
    if not postmortem:
        raise HTTPException(status_code=404, detail="Postmortem not found")
    if postmortem.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not your postmortem")

    for field, value in payload.model_dump(exclude_unset=True, exclude={"tags"}).items():
        setattr(postmortem, field, value)
    if payload.tags is not None:
        postmortem.tags = _get_or_create_tags(db, payload.tags)

    db.commit()
    db.refresh(postmortem)
    return postmortem


@router.delete("/{postmortem_id}")
def delete_postmortem(
    postmortem_id: uuid.UUID,
    db: Session = Depends(get_db),
    user_and_token=Depends(get_current_user_and_token),
):
    user, _ = user_and_token
    postmortem = db.query(Postmortem).filter(Postmortem.id == postmortem_id).first()
    if not postmortem:
        raise HTTPException(status_code=404, detail="Postmortem not found")
    if postmortem.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not your postmortem")

    db.delete(postmortem)
    db.commit()
    return {"status": "deleted"}
