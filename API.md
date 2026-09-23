# 🔌 API Reference

## The Technical Anti-Portfolio — FastAPI Backend

Base URL (local): `http://localhost:8000`

---

## Auth

### `GET /auth/github/login`
Redirects to GitHub OAuth consent screen.

### `GET /auth/github/callback`
Handles GitHub OAuth callback, creates/updates user, returns session token.

**Response**
```json
{ "access_token": "string", "user": { "id": "uuid", "username": "string" } }
```

---

## Repos & Commits

### `GET /repos`
Returns the authenticated user's GitHub repositories.

### `GET /repos/{owner}/{repo}/commits`
Returns commit history for a given repo.

### `GET /repos/{owner}/{repo}/compare/{base}...{head}`
Fetches and sanitizes the diff between two commits.

**Response**
```json
{
  "files": [
    { "file_path": "string", "faulty_chunk": "string", "resolved_chunk": "string" }
  ]
}
```

---

## Postmortems

### `POST /postmortems`
Create a new postmortem.

**Body**
```json
{
  "title": "string",
  "hypothesis": "string",
  "breaking_point": "string",
  "architectural_rule": "string",
  "diff_snippet_ids": ["uuid"],
  "tags": ["string"],
  "is_public": true
}
```

### `GET /postmortems/{id}`
Fetch a single postmortem with its diff snippets and tags.

### `PUT /postmortems/{id}`
Update an existing postmortem.

### `DELETE /postmortems/{id}`
Delete a postmortem.

### `GET /postmortems?tag={tag}`
List/filter postmortems by taxonomy tag.

---

## Public Profile

### `GET /u/{username}`
Returns all public postmortems for a given user — powers the `/u/:username` frontend page.

---

## Taxonomy Tags

### `GET /tags`
List all available taxonomy tags (e.g. `#RaceCondition`, `#MemoryLeak`, `#Deadlock`).

### `POST /tags`
Create a new tag (admin/maintainer use).

---

## Error Format

All errors follow a consistent shape:
```json
{ "error": "string", "detail": "string" }
```

## Rate Limits

GitHub API calls are subject to GitHub's own limit (5,000 req/hr per authenticated user). This backend does not currently implement additional rate limiting at MVP scale.
