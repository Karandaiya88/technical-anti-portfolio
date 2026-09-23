# 🔬 The Technical Anti-Portfolio

> An evidence-backed Root Cause Analysis (RCA) & Post-Mortem platform for engineers who want to show their debugging depth — not just their happy-path demos.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%2B%20Next.js%20%2B%20Postgres-informational)

---

## 💡 Why This Exists

Most developer portfolios show **completed, working things** — a to-do app, a clone, a CRUD dashboard. They run with one active user (`N=1`), so nothing ever breaks. Recruiters get zero signal on how you actually think under failure.

**The Technical Anti-Portfolio** flips that. It's a personal, searchable archive of:
- 🐛 Real bugs you hit (race conditions, memory leaks, deadlocks, bad assumptions)
- 🔍 The root cause, backed by an actual Git diff — not a story
- 🛠️ The fix, and the general engineering rule you took away from it

Instead of *"I built X,"* it answers *"here's proof I can diagnose and fix broken systems."*

---

## ✨ Core Features (MVP)

| Feature | Description |
|---|---|
| **GitHub OAuth Ingestion** | Connect a repo, pick a buggy commit and its fix commit |
| **Side-by-Side Diff Viewer** | Clean, syntax-highlighted diff of the faulty → resolved code |
| **Postmortem Editor** | Structured write-up: hypothesis, breaking point, architectural rule |
| **Taxonomy Tags** | Classify each postmortem (`#RaceCondition`, `#MemoryLeak`, `#Deadlock`, etc.) |
| **Public Profile Page** | Shareable link — the actual "anti-portfolio" recruiters can browse |

> Auto AST parsing, telemetry graphs, and Redis-scale caching are **intentionally deferred** — see [ROADMAP.md](./ROADMAP.md) for why.

---

## 🧱 Tech Stack

- **Frontend:** Next.js 14 · TypeScript · Tailwind CSS
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Auth:** GitHub OAuth
- **Diffing:** `diff2html` / `react-diff-viewer`
- **Deployment:** Vercel (frontend) + Render/Railway (backend + DB)

Full details in [ARCHITECTURE.md](./ARCHITECTURE.md).

---

## 📂 Project Docs

| Doc | Purpose |
|---|---|
| [PRD.md](./PRD.md) | Product requirements — what we're building and why |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System design, data flow, tech decisions |
| [SCHEMA.md](./SCHEMA.md) | PostgreSQL schema and entity relationships |
| [ROADMAP.md](./ROADMAP.md) | Phased build plan (MVP → v2 → stretch) |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | Setup, branching, and commit conventions |
| [API.md](./API.md) | Backend endpoint reference |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | Vercel + Render/Railway deploy guide |
| [SECURITY.md](./SECURITY.md) | Vulnerability reporting policy |
| [CHANGELOG.md](./CHANGELOG.md) | Version history |
| [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) | Community standards |
| [LICENSE](./LICENSE) | MIT License |

---

## 🚀 Quick Start

```bash
# clone
git clone https://github.com/Karandaiya88/technical-anti-portfolio.git
cd technical-anti-portfolio

# backend
cd backend && pip install -r requirements.txt
uvicorn main:app --reload

# frontend
cd frontend && npm install
npm run dev
```

---

## 👤 Author

**Karan Daiya** — B.Tech CSE, JIET Jodhpur
[GitHub](https://github.com/Karandaiya88) · [LinkedIn](https://linkedin.com/in/karan-d88) · [Portfolio](https://karandaiya.vercel.app)
