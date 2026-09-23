# 🚀 Deployment Guide

## The Technical Anti-Portfolio

---

## 1. Overview

| Layer | Platform |
|---|---|
| Frontend (Next.js) | Vercel |
| Backend (FastAPI) | Render or Railway |
| Database (PostgreSQL) | Render/Railway managed Postgres |

---

## 2. Prerequisites

- GitHub OAuth App registered (get `client_id` and `client_secret`)
- Vercel account linked to your GitHub repo
- Render or Railway account for backend + DB

---

## 3. Backend Deployment (Render/Railway)

1. Push code to GitHub (`main` branch).
2. Create a new **Web Service** on Render/Railway, connect the repo, set root directory to `backend/`.
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables:
   ```
   DATABASE_URL=postgres://...
   GITHUB_CLIENT_ID=...
   GITHUB_CLIENT_SECRET=...
   SECRET_KEY=...
   FRONTEND_URL=https://your-app.vercel.app
   ```
6. Provision a managed PostgreSQL instance, copy its connection string into `DATABASE_URL`.
7. Run migrations (Alembic, if used):
   ```bash
   alembic upgrade head
   ```

---

## 4. Frontend Deployment (Vercel)

1. Import the repo into Vercel, set root directory to `frontend/`.
2. Add environment variables:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.onrender.com
   NEXTAUTH_URL=https://your-app.vercel.app
   NEXTAUTH_SECRET=...
   GITHUB_CLIENT_ID=...
   GITHUB_CLIENT_SECRET=...
   ```
3. Deploy — Vercel auto-builds on every push to `main`.

---

## 5. Post-Deploy Checklist

- [ ] GitHub OAuth callback URL updated to production backend URL
- [ ] CORS configured on backend to allow the Vercel frontend origin
- [ ] Database migrations applied
- [ ] Public profile page (`/u/:username`) loads correctly in production
- [ ] Diff sanitization verified in production (no raw code execution)

---

## 6. Rollback

Both Vercel and Render/Railway keep previous deployment snapshots — use their dashboard to roll back to the last known-good deploy if something breaks.
