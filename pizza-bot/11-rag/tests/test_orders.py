"""Tests for orders.py. They never call Ollama."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

import orders  # noqa: E402
from orders import Order, parse_order, validate_order  # noqa: E402


def test_menu_pizzas_read_from_menu():
    assert len(orders.MENU_PIZZAS) == 8
    assert "Garden Veggie" in orders.MENU_PIZZAS and "BBQ Chicken" in orders.MENU_PIZZAS


def test_parse_order_builds_order_and_sends_schema(monkeypatch):
    seen = {}

    def fake_chat(messages, **kwargs):
        seen["messages"], seen["kwargs"] = messages, kwargs
        return {"role": "assistant", "content": json.dumps(
            {"pizza": "Margherita", "size": "large", "quantity": 2, "notes": "no olives"})}

    monkeypatch.setattr(orders, "chat", fake_chat)
    order = parse_order("Two large margheritas, no olives")
    assert order == Order("Margherita", "large", 2, "no olives")
    assert seen["kwargs"]["response_format"] == orders.ORDER_SCHEMA
    assert seen["messages"][0]["role"] == "system"
    assert seen["messages"][-1]["content"] == "Two large margheritas, no olives"


def test_validate_accepts_good_order():
    assert validate_order(Order("Hawaiian", "medium", 1, "")) == []


def test_validate_catches_pizza_not_on_menu():
    problems = validate_order(Order("large margheritas", "large", 2, ""))
    assert len(problems) == 1 and "not on the menu" in problems[0]


def test_validate_catches_bad_quantity():
    assert validate_order(Order("Margherita", "small", 0, ""))
    assert validate_order(Order("Margherita", "small", 11, ""))
