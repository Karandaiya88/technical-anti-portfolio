"""
Pydantic schemas — request/response shapes for the API.
"""
import uuid
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    username: str
    email: Optional[str] = None


class TagOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    name: str
    category: Optional[str] = None


class TagCreate(BaseModel):
    name: str
    category: Optional[str] = None


class DiffSnippetOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    file_path: str
    faulty_chunk: Optional[str] = None
    resolved_chunk: Optional[str] = None


class DiffSnippetCreate(BaseModel):
    file_path: str
    faulty_chunk: Optional[str] = None
    resolved_chunk: Optional[str] = None


class PostmortemCreate(BaseModel):
    title: str
    hypothesis: Optional[str] = None
    breaking_point: Optional[str] = None
    architectural_rule: Optional[str] = None
    is_public: bool = True
    tags: List[str] = []
    diff_snippets: List[DiffSnippetCreate] = []


class PostmortemUpdate(BaseModel):
    title: Optional[str] = None
    hypothesis: Optional[str] = None
    breaking_point: Optional[str] = None
    architectural_rule: Optional[str] = None
    is_public: Optional[bool] = None
    tags: Optional[List[str]] = None


class PostmortemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    title: str
    hypothesis: Optional[str] = None
    breaking_point: Optional[str] = None
    architectural_rule: Optional[str] = None
    is_public: bool
    created_at: datetime
    tags: List[TagOut] = []
    diff_snippets: List[DiffSnippetOut] = []


class CompareRequest(BaseModel):
    owner: str
    repo: str
    base: str
    head: str
