"""
Sanitizes fetched/user-submitted code before it is stored or rendered.

Security requirement (see SECURITY.md / ARCHITECTURE.md):
- No raw code is ever passed to the frontend without escaping.
- No client-side eval() is possible if this layer does its job.
"""
import bleach

# Lockfiles / generated files we never want to store as "diff content"
IGNORED_FILE_PATTERNS = (
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "poetry.lock",
    "Cargo.lock",
    ".min.js",
    ".map",
)


def is_ignored_file(file_path: str) -> bool:
    return any(pattern in file_path for pattern in IGNORED_FILE_PATTERNS)


def sanitize_code_chunk(raw: str) -> str:
    """
    Escapes any HTML/script content in a code chunk so it can never execute
    when rendered on the frontend. The frontend diff viewer is responsible
    for syntax highlighting on top of this already-safe text.
    """
    if raw is None:
        return ""
    # Strip all tags — code should render as plain text, syntax highlighting
    # happens client-side against escaped text, never innerHTML from source.
    return bleach.clean(raw, tags=[], strip=True)


def enforce_size_limit(raw: str, max_kb: int) -> str:
    """Truncates content that exceeds the configured max diff size."""
    max_bytes = max_kb * 1024
    encoded = raw.encode("utf-8")
    if len(encoded) <= max_bytes:
        return raw
    return encoded[:max_bytes].decode("utf-8", errors="ignore") + "\n... [truncated: exceeds size limit]"
