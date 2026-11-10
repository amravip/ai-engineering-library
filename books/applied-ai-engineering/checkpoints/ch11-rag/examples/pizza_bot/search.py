"""Chapter 11: find the shop documents that match a question."""

from pathlib import Path

from model import embed
from vectors import cosine_similarity

STOP_WORDS = {"a", "an", "the", "is", "are", "do", "does", "you", "i", "can", "my",
              "to", "of", "in", "on", "for", "and", "or", "it", "we", "your", "what",
              "how", "get", "with", "at", "if", "be", "me"}


def load_documents(folder: str | Path) -> dict[str, str]:
    """Read every .txt file in `folder`, keyed by file name."""
    paths = sorted(Path(folder).glob("*.txt"))
    return {path.name: path.read_text(encoding="utf-8") for path in paths}


def words_of(text: str) -> set[str]:
    """Lower-case words with punctuation stripped and stop words removed."""
    cleaned = (word.strip(".,?!:;\"'()£-") for word in text.lower().split())
    return {word for word in cleaned if word and word not in STOP_WORDS}


def keyword_search(question: str, documents: dict[str, str], top: int = 2) -> list[tuple[str, int]]:
    """Rank documents by how many question words they share."""
    question_words = words_of(question)
    scores = {name: len(question_words & words_of(text)) for name, text in documents.items()}
    return sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))[:top]


def embedding_search(question: str, documents: dict[str, str], top: int = 2) -> list[tuple[str, float]]:
    """Rank documents by embedding similarity to the question.

    This embeds every document on every call. That is fine for eight short
    files; a real system embeds the documents once and stores the vectors.
    """
    names = list(documents)
    vectors = embed([question] + [documents[name] for name in names])
    scores = {name: cosine_similarity(vectors[0], vector) for name, vector in zip(names, vectors[1:])}
    return sorted(scores.items(), key=lambda pair: -pair[1])[:top]
