# 🔒 Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| `main` (latest) | ✅ |
| Older/archived | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability in this project — especially around:
- Diff sanitization / stored code injection
- GitHub OAuth token handling
- Any client-side execution of user-submitted content

please **do not open a public issue**. Instead, report it privately via a [GitHub Security Advisory](https://github.com/Karandaiya88/technical-anti-portfolio/security/advisories) or by contacting the maintainer directly.

## Key Security Principles in This Project

- **Zero client-side `eval()`** on any fetched or user-submitted code.
- All diff content is **tokenized and sanitized server-side** before being rendered on the frontend.
- OAuth tokens are stored encrypted and never exposed to the client.
- Diff payloads are size-limited (max 250 KB per commit pair) to prevent abuse.

Response time for verified reports: best-effort, typically within a few days (solo-maintained project).
