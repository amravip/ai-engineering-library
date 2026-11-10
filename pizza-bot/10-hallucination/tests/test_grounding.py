"""Tests for grounding.py. They never call Ollama."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

from grounding import menu_names, unsupported_pizzas  # noqa: E402

MENU = (Path(__file__).parents[1] / "examples" / "pizza_bot" / "menu.txt").read_text(encoding="utf-8")


def test_menu_names():
    assert menu_names(MENU)[:2] == ["Margherita", "Garden Veggie"]


def test_real_menu_items_are_not_flagged():
    answer = "- Margherita (£9) - tomato\n- Garden Veggie (£11) - peppers"
    assert unsupported_pizzas(answer, MENU) == []


def test_invented_pizza_is_flagged():
    answer = "1. **Vegan Supreme** - lots of veg\n2. **Mushroom Pizza**: nice"
    assert unsupported_pizzas(answer, MENU) == ["Vegan Supreme"]


def test_indented_details_and_long_sentences_are_ignored():
    answer = "- Mushroom\n   - Sautéed spinach and cheese\n- We also offer a great many extras today"
    assert unsupported_pizzas(answer, MENU) == []
