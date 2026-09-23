"""
Repo, commit, and diff-comparison endpoints (GitHub Ingestion Engine).
"""
from fastapi import APIRouter, Depends

from app.config import settings
from app.deps import get_current_user_and_token
from app.github_client import GitHubClient
from app.utils.sanitize import sanitize_code_chunk, enforce_size_limit, is_ignored_file

router = APIRouter(prefix="/repos", tags=["repos"])


@router.get("")
async def list_repos(user_and_token=Depends(get_current_user_and_token)):
    _, github_token = user_and_token
    client = GitHubClient(access_token=github_token)
    return await client.list_repos()


@router.get("/{owner}/{repo}/commits")
async def list_commits(owner: str, repo: str, user_and_token=Depends(get_current_user_and_token)):
    _, github_token = user_and_token
    client = GitHubClient(access_token=github_token)
    return await client.list_commits(owner, repo)


@router.get("/{owner}/{repo}/compare/{base}...{head}")
async def compare_commits(
    owner: str, repo: str, base: str, head: str,
    user_and_token=Depends(get_current_user_and_token),
):
    """
    Fetches the diff between two commits, strips lockfiles/binary noise,
    sanitizes each chunk, and enforces the configured size limit.
    """
    _, github_token = user_and_token
    client = GitHubClient(access_token=github_token)
    raw = await client.compare_commits(owner, repo, base, head)

    files = []
    for f in raw.get("files", []):
        file_path = f.get("filename", "")
        if is_ignored_file(file_path):
            continue
        patch = f.get("patch", "")
        patch = enforce_size_limit(patch, settings.max_diff_size_kb)
        patch = sanitize_code_chunk(patch)
        files.append({
            "file_path": file_path,
            "status": f.get("status"),
            "patch": patch,
        })

    return {"files": files}
