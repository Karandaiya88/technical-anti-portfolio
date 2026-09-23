# 🤝 Contributing

## The Technical Anti-Portfolio

This is currently a solo/personal project, but this doc keeps development structured — and makes the repo look and behave like a real, maintained project.

---

## 1. Local Setup

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Docker (optional but recommended)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env       # fill in GitHub OAuth + DB credentials
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

---

## 2. Branching Strategy

- `main` — always deployable
- `dev` — active development, merges into `main` when stable
- `feature/<short-name>` — one branch per feature (e.g. `feature/diff-viewer`)
- `fix/<short-name>` — bug fixes

## 3. Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add GitHub commit-pair diff fetch
fix: sanitize diff output before render
docs: update SCHEMA.md with taxonomy_tags join table
chore: bump dependencies
```

## 4. Code Style

- **Frontend:** ESLint + Prettier (`npm run lint`)
- **Backend:** `black` + `ruff` for formatting/linting
- Keep components and endpoints small and single-purpose

## 5. Pull Request Checklist

- [ ] Code builds and runs locally
- [ ] No secrets/credentials committed
- [ ] Diff sanitization untouched or improved — never bypassed
- [ ] Relevant doc (`PRD.md` / `ARCHITECTURE.md` / `SCHEMA.md`) updated if behavior changed

## 6. Security Notes

- Never render fetched or user-submitted code via client-side `eval()`.
- All diff content must pass through server-side sanitization before reaching the frontend.
- Do not commit `.env` files or GitHub OAuth secrets.
