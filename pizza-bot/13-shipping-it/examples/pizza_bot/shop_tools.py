"""The things the bot can do besides talk."""

import json
from pathlib import Path

ORDERS = json.loads(Path(__file__).with_name("orders.json").read_text(encoding="utf-8"))


def check_order(order_number: int) -> dict:
    """Look up an order by number, or return an error the model can read."""
    for order in ORDERS:
        if order["number"] == order_number:
            return order
    return {"error": f"No order with number {order_number}"}


def count_letter(text: str, letter: str) -> int:
    """Count a letter exactly, which a model reading tokens cannot do reliably."""
    return text.lower().count(letter.lower())


TOOLS = [
    {"type": "function", "function": {
        "name": "check_order",
        "description": "Look up an order's pizzas, total and status by its number.",
        "parameters": {"type": "object",
                       "properties": {"order_number": {"type": "integer"}},
                       "required": ["order_number"]}}},
    {"type": "function", "function": {
        "name": "count_letter",
        "description": "Count how many times a letter appears in a piece of text.",
        "parameters": {"type": "object",
                       "properties": {"text": {"type": "string"}, "letter": {"type": "string"}},
                       "required": ["text", "letter"]}}},
]

FUNCTIONS = {"check_order": check_order, "count_letter": count_letter}


def run_tool(name: str, arguments: dict) -> str:
    """Run one tool and return its result as a JSON string."""
    if name not in FUNCTIONS:
        return json.dumps({"error": f"Unknown tool {name}"})
    try:
        return json.dumps(FUNCTIONS[name](**arguments))
    except (TypeError, ValueError) as problem:
        return json.dumps({"error": f"Bad arguments for {name}: {problem}"})
