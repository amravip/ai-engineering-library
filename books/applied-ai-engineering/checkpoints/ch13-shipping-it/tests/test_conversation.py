"""Tests for conversation.py. They never call Ollama."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

from conversation import add_message, estimate_tokens, trim_history  # noqa: E402


def words(text):
    return len(text.split())


def make_history():
    history = [{"role": "system", "content": "be nice"}]
    for turn in ["one two", "three four", "five six"]:
        add_message(history, "user", turn)
    return history


def test_estimate_tokens_is_about_four_characters_each():
    assert estimate_tokens("a" * 40) == 10
    assert estimate_tokens("") == 1


def test_trim_does_nothing_when_it_fits():
    history = make_history()
    assert trim_history(history, 100, words) == history


def test_trim_drops_oldest_turns_first():
    trimmed = trim_history(make_history(), 6, words)
    assert [m["content"] for m in trimmed] == ["be nice", "three four", "five six"]


def test_trim_always_keeps_system_message():
    trimmed = trim_history(make_history(), 1, words)
    assert trimmed == [{"role": "system", "content": "be nice"}]


def test_trim_does_not_change_original():
    history = make_history()
    trim_history(history, 3, words)
    assert len(history) == 4
