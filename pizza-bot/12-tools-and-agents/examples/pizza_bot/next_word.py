"""A tiny language model that learns by counting which word follows which."""

import math
import re
from collections import Counter

FLOOR = 0.01  # probability given to a pair the model has never seen


def split_words(line: str) -> list[str]:
    """Lower-case words only: no capitals, no punctuation."""
    return re.findall(r"[a-z']+", line.lower())


def train_next_word(text: str) -> dict[str, Counter]:
    """Count, line by line, how often each word is followed by each other word."""
    counts: dict[str, Counter] = {}
    for line in text.splitlines():
        words = split_words(line)
        for current, following in zip(words, words[1:]):
            counts.setdefault(current, Counter())[following] += 1
    return counts


def next_word_probabilities(counts: dict[str, Counter], word: str) -> dict[str, float]:
    """Turn the counts after `word` into probabilities that add up to 1."""
    following = counts.get(word, Counter())
    total = sum(following.values())
    return {other: n / total for other, n in following.most_common()}


def generate(counts: dict[str, Counter], start: str, length: int) -> str:
    """Greedy generation: always take the most likely next word."""
    words = [start]
    for _ in range(length):
        probabilities = next_word_probabilities(counts, words[-1])
        if not probabilities:
            break  # the model has never seen this word followed by anything
        words.append(next(iter(probabilities)))  # most_common order: biggest first
    return " ".join(words)


def vocabulary_size(counts: dict[str, Counter]) -> int:
    """How many different words the model has seen."""
    seen = set(counts)
    for following in counts.values():
        seen.update(following)
    return len(seen)


def average_surprise(counts: dict[str, Counter] | None, lines: list[str],
                     vocabulary: int) -> float:
    """The toy's loss: average -ln(probability) of the word that really came next.

    An untrained model (counts=None) says every word is equally likely.
    """
    total, pairs = 0.0, 0
    for line in lines:
        words = split_words(line)
        for current, actual in zip(words, words[1:]):
            if counts is None:
                probability = 1 / vocabulary
            else:
                probability = next_word_probabilities(counts, current).get(actual, FLOOR)
            total += -math.log(probability)
            pairs += 1
    return total / pairs
