"""Measure how similar two lists of numbers (vectors) are."""

import math


def dot(a: list[float], b: list[float]) -> float:
    """Multiply matching numbers and add up the results."""
    return sum(x * y for x, y in zip(a, b))


def length(a: list[float]) -> float:
    """How long the arrow drawn by the vector is."""
    return math.sqrt(dot(a, a))


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """1.0 means the vectors point the same way, 0.0 means unrelated."""
    return dot(a, b) / (length(a) * length(b))
