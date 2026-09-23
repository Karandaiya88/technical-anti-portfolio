"""
SQLAlchemy ORM models — mirrors SCHEMA.md.
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    Column, String, Text, Boolean, ForeignKey, DateTime, Table
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base

# Many-to-many join table: postmortems <-> taxonomy_tags
postmortem_tags = Table(
    "postmortem_tags",
    Base.metadata,
    Column("postmortem_id", UUID(as_uuid=True), ForeignKey("postmortems.id"), primary_key=True),
    Column("tag_id", UUID(as_uuid=True), ForeignKey("taxonomy_tags.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    github_id = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    postmortems = relationship("Postmortem", back_populates="user", cascade="all, delete-orphan")


class Postmortem(Base):
    __tablename__ = "postmortems"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    hypothesis = Column(Text, nullable=True)
    breaking_point = Column(Text, nullable=True)
    architectural_rule = Column(Text, nullable=True)
    is_public = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="postmortems")
    diff_snippets = relationship("DiffSnippet", back_populates="postmortem", cascade="all, delete-orphan")
    tags = relationship("TaxonomyTag", secondary=postmortem_tags, back_populates="postmortems")


class DiffSnippet(Base):
    __tablename__ = "diff_snippets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    postmortem_id = Column(UUID(as_uuid=True), ForeignKey("postmortems.id"), nullable=False)
    file_path = Column(String, nullable=False)
    faulty_chunk = Column(Text, nullable=True)
    resolved_chunk = Column(Text, nullable=True)

    postmortem = relationship("Postmortem", back_populates="diff_snippets")


class TaxonomyTag(Base):
    __tablename__ = "taxonomy_tags"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=True)

    postmortems = relationship("Postmortem", secondary=postmortem_tags, back_populates="tags")
