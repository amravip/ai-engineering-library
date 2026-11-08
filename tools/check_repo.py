"""Check the repository layout and wording. Standard library only; CI runs this.

Usage (from any folder):
    python tools/check_repo.py

Prints one line per problem and exits with status 1 when any check fails.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THIS_FILE = Path(__file__).resolve()

# Folder slug and exact title, in catalogue order.
BOOKS = [
    ("applied-ai-engineering", "Applied AI Engineering"),
    ("prompt-and-context-engineering", "Prompt & Context Engineering"),
    ("rag-engineering", "RAG Engineering"),
    ("ai-agent-engineering", "AI Agent Engineering"),
    ("model-context-protocol", "Model Context Protocol"),
    ("ai-harness-engineering", "AI Harness Engineering"),
    ("multi-agent-systems", "Multi-Agent Systems"),
    ("ai-agent-workflows", "AI Agent Workflows"),
    ("llmops", "LLMOps"),
    ("ai-security", "AI Security"),
    ("ai-system-design", "AI System Design"),
    ("multimodal-ai", "Multimodal AI"),
]

# Folders that hold authoring material and must never appear in this repository.
FORBIDDEN_FOLDERS = {"manuscript", "reviews", "planning", "cover", "dist"}
FORBIDDEN_FILE_SUFFIXES = {".epub", ".pdf"}
FORBIDDEN_FILE_NAMES = {".env"}

SKIPPED_FOLDERS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", ".venv", "venv",
                   "node_modules", ".astro"}
# Build output of the website. It is gitignored, rebuilt by `npm run build`, and never committed.
SKIPPED_PATHS = {("website", "dist")}
PLACEHOLDER_PATTERN = re.compile(r"\b(TODO|TBD|FIXME|placeholder)\b", re.IGNORECASE)


def repository_files() -> list[Path]:
    """Every file in the repository, leaving out tool caches and virtual environments."""
    files = []
    for path in ROOT.rglob("*"):
        relative_parts = path.relative_to(ROOT).parts
        if SKIPPED_FOLDERS & set(relative_parts):
            continue
        if relative_parts[:2] in [tuple(item) for item in SKIPPED_PATHS]:
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def check_book_folders(problems: list[str]) -> None:
    for slug, title in BOOKS:
        readme = ROOT / "books" / slug / "README.md"
        if not readme.is_file():
            problems.append(f"missing books/{slug}/README.md")
        elif title not in readme.read_text(encoding="utf-8"):
            problems.append(f"books/{slug}/README.md does not mention its title '{title}'")


def check_checkpoints(problems: list[str]) -> None:
    for checkpoint in sorted((ROOT / "books").glob("*/checkpoints/*")):
        if not checkpoint.is_dir():
            continue
        relative = checkpoint.relative_to(ROOT).as_posix()
        if not (checkpoint / "README.md").is_file():
            problems.append(f"missing {relative}/README.md")
        for folder in ("examples", "tests"):
            if not (checkpoint / folder).is_dir():
                problems.append(f"missing {relative}/{folder}/")


def check_forbidden_paths(files: list[Path], problems: list[str]) -> None:
    for path in files:
        relative = path.relative_to(ROOT)
        folders = set(relative.parts[:-1])
        for folder in sorted(folders & FORBIDDEN_FOLDERS):
            problems.append(f"forbidden folder '{folder}' in {relative.as_posix()}")
        if path.suffix.lower() in FORBIDDEN_FILE_SUFFIXES:
            problems.append(f"forbidden file type in {relative.as_posix()}")
        if path.name in FORBIDDEN_FILE_NAMES or path.name.startswith(".env."):
            problems.append(f"forbidden secrets file {relative.as_posix()}")


def check_placeholders(files: list[Path], problems: list[str]) -> None:
    for path in files:
        if path == THIS_FILE:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binary file such as an image
        for number, line in enumerate(text.splitlines(), start=1):
            match = PLACEHOLDER_PATTERN.search(line)
            if match:
                relative = path.relative_to(ROOT).as_posix()
                problems.append(f"'{match.group(0)}' text in {relative}:{number}")


def check_root_readme(problems: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        problems.append("missing README.md")
        return
    text = readme.read_text(encoding="utf-8")
    for _, title in BOOKS:
        if title not in text:
            problems.append(f"README.md does not list '{title}'")


def main() -> int:
    files = repository_files()
    problems: list[str] = []
    check_book_folders(problems)
    check_checkpoints(problems)
    check_forbidden_paths(files, problems)
    check_placeholders(files, problems)
    check_root_readme(problems)

    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        print(f"{len(problems)} problem(s) found")
        return 1
    print(f"Repository checks passed ({len(files)} files, {len(BOOKS)} books)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
