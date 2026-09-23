"""
Thin wrapper around the GitHub REST API for repo/commit/diff fetching.
"""
import httpx

GITHUB_API = "https://api.github.com"


class GitHubClient:
    def __init__(self, access_token: str):
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/vnd.github+json",
        }

    async def list_repos(self):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{GITHUB_API}/user/repos", headers=self.headers, params={"sort": "updated"})
            resp.raise_for_status()
            return resp.json()

    async def list_commits(self, owner: str, repo: str):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{GITHUB_API}/repos/{owner}/{repo}/commits", headers=self.headers)
            resp.raise_for_status()
            return resp.json()

    async def compare_commits(self, owner: str, repo: str, base: str, head: str):
        """
        Calls /repos/{owner}/{repo}/compare/{base}...{head}
        Returns the raw comparison payload (includes per-file patches).
        """
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                f"{GITHUB_API}/repos/{owner}/{repo}/compare/{base}...{head}",
                headers=self.headers,
            )
            resp.raise_for_status()
            return resp.json()

    async def exchange_code_for_token(self, code: str, client_id: str, client_secret: str, redirect_uri: str):
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "https://github.com/login/oauth/access_token",
                headers={"Accept": "application/json"},
                data={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
            )
            resp.raise_for_status()
            return resp.json()

    async def get_authenticated_user(self):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{GITHUB_API}/user", headers=self.headers)
            resp.raise_for_status()
            return resp.json()
