"""Tests for attention. No Ollama."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

from attention import attend, attention_weights, softmax  # noqa: E402


def test_softmax_adds_to_one_and_keeps_order():
    weights = softmax([1.0, 2.0, 3.0])
    assert math.isclose(sum(weights), 1.0)
    assert weights[0] < weights[1] < weights[2]


def test_softmax_handles_large_scores():
    assert math.isclose(sum(softmax([1000.0, 1001.0])), 1.0)


def test_attention_looks_at_the_matching_key():
    weights = attention_weights([1, 0], [[5, 0], [0, 5]])
    assert weights[0] > 0.99


def test_attend_blends_values():
    result = attend([0, 0], [[1, 1], [1, 1]], [[2, 0], [0, 2]])
    assert result == [1.0, 1.0]
