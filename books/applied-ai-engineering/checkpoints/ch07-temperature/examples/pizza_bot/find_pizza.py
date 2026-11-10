"""Chapter 3: find menu lines by meaning, not by matching words."""

import re
from pathlib import Path

from model import embed
from vectors import cosine_similarity

menu = Path(__file__).with_name("menu.txt").read_text(encoding="utf-8")
lines = [line for line in menu.splitlines()[1:] if line.strip()]
line_vectors = embed([" ".join(line.split()) for line in lines])


def best_matches(phrase: str, top: int = 3) -> list[tuple[float, str]]:
    """Rank every menu line by similarity to the customer's phrase."""
    phrase_vector = embed([phrase])[0]
    names = [re.split(r"\s{2,}", line)[0] for line in lines]  # text before the gap
    scored = [(cosine_similarity(phrase_vector, vector), name)
              for name, vector in zip(names, line_vectors)]
    return sorted(scored, reverse=True)[:top]


for phrase in ["something without meat", "I love cheese", "a spicy one"]:
    print(f"Customer: {phrase}")
    for score, name in best_matches(phrase):
        print(f"  {score:.2f}  {name}")
