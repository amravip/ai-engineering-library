"""Tests for the Exercise 5 solution. They use the step 8 code and never call Ollama."""

import sys
from pathlib import Path

CHECKPOINT_CODE = Path(__file__).parents[3] / "08-talking-to-models-from-code" / "examples" / "pizza_bot"
sys.path.insert(0, str(CHECKPOINT_CODE))
sys.path.insert(0, str(Path(__file__).parents[1] / "solutions"))

from ex05_pizza_enum import menu_order_schema  # noqa: E402
from orders import MENU_PIZZAS, ORDER_SCHEMA, Order, validate_order  # noqa: E402


def test_pizza_enum_is_the_menu():
    assert menu_order_schema()["properties"]["pizza"]["enum"] == MENU_PIZZAS
    assert len(MENU_PIZZAS) == 8


def test_other_fields_are_unchanged():
    schema = menu_order_schema()
    assert schema["properties"]["size"] == ORDER_SCHEMA["properties"]["size"]
    assert schema["required"] == ORDER_SCHEMA["required"]


def test_original_schema_is_not_changed():
    menu_order_schema()
    assert "enum" not in ORDER_SCHEMA["properties"]["pizza"]


def test_vegan_supreme_is_not_allowed_by_the_enum():
    assert "Vegan Supreme" not in menu_order_schema()["properties"]["pizza"]["enum"]
    assert validate_order(Order("Vegan Supreme", "large", 1, "")) == [
        "'Vegan Supreme' is not on the menu"
    ]
