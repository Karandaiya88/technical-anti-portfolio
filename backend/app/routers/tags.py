"""
Taxonomy tag listing/creation.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import TaxonomyTag
from app.schemas import TagOut, TagCreate

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("", response_model=list[TagOut])
def list_tags(db: Session = Depends(get_db)):
    return db.query(TaxonomyTag).order_by(TaxonomyTag.category, TaxonomyTag.name).all()


@router.post("", response_model=TagOut)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)):
    tag = TaxonomyTag(name=payload.name, category=payload.category)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag
