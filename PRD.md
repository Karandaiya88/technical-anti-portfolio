# 📋 Product Requirements Document (PRD)

## The Technical Anti-Portfolio

---

## 1. Overview

| | |
|---|---|
| **Product** | The Technical Anti-Portfolio |
| **Domain** | Developer Tooling · Engineering Reliability |
| **Owner** | Karan Daiya |
| **Status** | MVP scoping |

**One-liner:** A platform where engineers document real production failures — with Git-backed proof — instead of listing finished projects.

---

## 2. Problem Statement

- Tutorial and portfolio projects run with `N=1` active users, so race conditions, deadlocks, and edge cases never surface.
- Recruiters and interviewers have no reliable signal on how a candidate debugs a system under real failure conditions.
- Engineers often fix hard bugs through trial and error, then never document *why* the fix worked — so the lesson is lost and the same mistake repeats in the next project.

## 3. Goals

1. Let a user connect a GitHub repo and select a "before" (buggy) and "after" (fixed) commit.
2. Auto-generate a diff view between the two commits.
3. Let the user write a structured postmortem around that diff.
4. Tag each postmortem by failure category for browsability.
5. Expose a clean, public, shareable profile page — the actual artifact recruiters look at.

### Non-Goals (for MVP)

- Automated root-cause detection via AST analysis (manual tagging only, for now)
- Real production telemetry integration (RAM/latency graphs) — mockups are **not** included in MVP to avoid misleading viewers
- Multi-user collaboration / teams
- Public submission marketplace (this is a personal tool, not a crowd-sourced platform, at least initially)

---

## 4. User Stories

- **As a student engineer**, I want to import a specific commit pair from my GitHub repo, so I can generate a diff without manually copy-pasting code.
- **As a student engineer**, I want to write a postmortem (hypothesis → breaking point → fix → rule learned), so I can turn a debugging session into a permanent artifact.
- **As a recruiter/interviewer**, I want to browse a candidate's postmortems by tag, so I can quickly assess their debugging depth in a specific area (e.g., concurrency).
- **As a returning user**, I want to see all my past postmortems in one searchable list, so I can reuse the "engineering rules" I've derived across future projects.

---

## 5. Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | GitHub OAuth login | Must |
| FR-2 | Fetch repo list + commit history via GitHub API | Must |
| FR-3 | Select two commits, generate unified diff | Must |
| FR-4 | Create/edit/delete a postmortem tied to a diff | Must |
| FR-5 | Tag postmortems with taxonomy labels | Must |
| FR-6 | Public read-only profile page (`/u/:username`) | Must |
| FR-7 | Filter/search postmortems by tag | Should |
| FR-8 | Markdown support in postmortem body | Should |
| FR-9 | Auto-suggest tags from diff content (AST-based) | Could (v2) |
| FR-10 | Telemetry graph overlays | Won't (MVP) |

---

## 6. Success Metrics (personal-project scale)

- At least **5–8 real postmortems** published from Karan's own project history within MVP phase.
- Profile page is live and linkable from resume/LinkedIn.
- Page loads and diff renders correctly for repos up to typical student-project size (no perf benchmarking needed at this stage).

---

## 7. Constraints

- Solo developer, limited timeline — scope is deliberately reduced vs. original system spec (see [ROADMAP.md](./ROADMAP.md)).
- GitHub API rate limits (5,000 req/hr authenticated) — acceptable for single-user MVP, revisit if scaled.
- Must not execute any client-side `eval()` on fetched diff content — sanitize all rendered code (security requirement, not optional).

---

## 8. Out of Scope Risks Acknowledged

- Original spec's Redis caching, OAuth token pooling, and AST engine are real engineering needs **only at multi-user scale**. Building them now for a single-user MVP would be premature optimization — explicitly deferred.
