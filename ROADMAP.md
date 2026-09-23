# 🗺️ Roadmap

## The Technical Anti-Portfolio

Scope is deliberately phased — the original spec (AST engine, telemetry, Redis-scale caching) is a multi-person, multi-month effort. This roadmap ships a real, working, demo-able tool first, then layers in complexity only if there's a reason to.

---

## Phase 0 — Setup (Week 1)
- [ ] Repo scaffolding (`frontend/`, `backend/`)
- [ ] GitHub OAuth app registration
- [ ] PostgreSQL schema migration (see [SCHEMA.md](./SCHEMA.md))
- [ ] Basic FastAPI + Next.js boilerplate wired together

## Phase 1 — MVP Core (Weeks 2–3)
- [ ] GitHub OAuth login flow (frontend + backend)
- [ ] Repo + commit list fetch from GitHub API
- [ ] Commit-pair diff fetch (`/compare/{base}...{head}`)
- [ ] Diff sanitization + rendering (`react-diff-viewer`)
- [ ] Postmortem CRUD (create/edit/delete)
- [ ] Manual taxonomy tagging

## Phase 2 — Public Profile (Week 4)
- [ ] Public read-only profile page (`/u/:username`)
- [ ] Tag-based filtering/search on profile
- [ ] Markdown rendering in postmortem body
- [ ] Basic responsive design pass (mobile-friendly)
- [ ] Deploy: Vercel (frontend) + Render/Railway (backend + DB)

## Phase 3 — Seed Content (Week 5)
- [ ] Write 5–8 real postmortems from Karan's own past bugs (ARIC, F1 Analytics, TalentTrail, etc.)
- [ ] Polish UI/UX, add empty states, loading states
- [ ] Add link to profile from resume + LinkedIn + personal portfolio site

---

## v2 — Stretch Goals (post-MVP, only if there's a clear reason to build them)
- [ ] AST-based auto-tagging (distinguish structural vs. cosmetic diffs)
- [ ] Complexity scoring to filter low-quality/whitespace-only submissions
- [ ] Redis edge caching for repeated diff fetches
- [ ] GitHub OAuth token pooling (only relevant at multi-user scale)
- [ ] Real telemetry integration (opt-in, clearly labeled as real data — never mocked)

---

## Explicitly Not Planned
- Multi-tenant / crowd-sourced marketplace of postmortems
- Real-time collaboration features
- Anything requiring infrastructure beyond a single Postgres instance at this stage
