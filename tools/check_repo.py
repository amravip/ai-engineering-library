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

LEARNING_PATH = ROOT / "pizza-bot"
STEP_FOLDER = re.compile(r"^\d{2}-[a-z0-9-]+$")

# Folders that hold drafts, other projects or build output, and must never appear in this repository.
FORBIDDEN_FOLDERS = {"manuscript", "reviews", "planning", "cover", "dist", "books", "website"}
FORBIDDEN_FILE_SUFFIXES = {".epub", ".pdf"}
FORBIDDEN_FILE_NAMES = {".env"}

SKIPPED_FOLDERS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache", ".venv", "venv", "node_modules"}
PLACEHOLDER_PATTERN = re.compile(r"\b(TODO|TBD|FIXME|placeholder)\b", re.IGNORECASE)
# The examples are code only. None of these words belongs in any text file, plurals included.
WORDING_PATTERN = re.compile(r"\b(books?|chapters?|listings?|volumes?|editions?|appendix|appendices)\b", re.IGNORECASE)


def repository_files() -> list[Path]:
    """Every file in the repository, leaving out tool caches and virtual environments."""
    files = []
    for path in ROOT.rglob("*"):
        relative_parts = path.relative_to(ROOT).parts
        if SKIPPED_FOLDERS & set(relative_parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def step_folders() -> list[Path]:
    return sorted(p for p in LEARNING_PATH.iterdir() if p.is_dir() and STEP_FOLDER.match(p.name))


def check_learning_path(problems: list[str]) -> None:
    if not (LEARNING_PATH / "README.md").is_file():
        problems.append("missing pizza-bot/README.md")
    if not (LEARNING_PATH / "requirements-dev.txt").is_file():
        problems.append("missing pizza-bot/requirements-dev.txt")
    steps = step_folders()
    if not steps:
        problems.append("no step folders (NN-name) in pizza-bot/")
    for step in steps:
        relative = step.relative_to(ROOT).as_posix()
        if not (step / "README.md").is_file():
            problems.append(f"missing {relative}/README.md")
        for folder in ("examples", "tests"):
            if not (step / folder).is_dir():
                problems.append(f"missing {relative}/{folder}/")


def check_exercises(problems: list[str]) -> None:
    for exercise in sorted((LEARNING_PATH / "exercises").glob("*/")):
        relative = exercise.relative_to(ROOT).as_posix()
        if not (exercise / "README.md").is_file():
            problems.append(f"missing {relative}/README.md")
        if not (exercise / "tests").is_dir():
            problems.append(f"missing {relative}/tests/")


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


def read_text_files(files: list[Path]) -> list[tuple[Path, str]]:
    """The text of every file that decodes as UTF-8. Binary files such as images are skipped."""
    texts = []
    for path in files:
        if path == THIS_FILE:
            continue
        try:
            texts.append((path, path.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            continue
    return texts


def check_placeholders(texts: list[tuple[Path, str]], problems: list[str]) -> None:
    for path, text in texts:
        for number, line in enumerate(text.splitlines(), start=1):
            match = PLACEHOLDER_PATTERN.search(line)
            if match:
                relative = path.relative_to(ROOT).as_posix()
                problems.append(f"'{match.group(0)}' text in {relative}:{number}")


def check_wording(texts: list[tuple[Path, str]], problems: list[str]) -> None:
    for path, text in texts:
        for number, line in enumerate(text.splitlines(), start=1):
            match = WORDING_PATTERN.search(line)
            if match:
                relative = path.relative_to(ROOT).as_posix()
                problems.append(f"banned word '{match.group(0)}' in {relative}:{number}")


def check_root_readme(problems: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        problems.append("missing README.md")
        return
    text = readme.read_text(encoding="utf-8")
    for step in step_folders():
        if step.name not in text:
            problems.append(f"README.md does not link to step '{step.name}'")


def main() -> int:
    files = repository_files()
    texts = read_text_files(files)
    problems: list[str] = []
    check_learning_path(problems)
    check_exercises(problems)
    check_forbidden_paths(files, problems)
    check_placeholders(texts, problems)
    check_wording(texts, problems)
    check_root_readme(problems)

    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        print(f"{len(problems)} problem(s) found")
        return 1
    print(f"Repository checks passed ({len(files)} files, {len(step_folders())} steps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
