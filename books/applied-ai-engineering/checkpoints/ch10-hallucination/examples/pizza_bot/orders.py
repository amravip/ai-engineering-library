"""Chapter 8: turn a customer's sentence into an Order a program can use."""

import json
from dataclasses import dataclass
from pathlib import Path

from model import chat


@dataclass
class Order:
    pizza: str
    size: str
    quantity: int
    notes: str


ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "pizza": {"type": "string"},
        "size": {"type": "string", "enum": ["small", "medium", "large"]},
        "quantity": {"type": "integer"},
        "notes": {"type": "string"},
    },
    "required": ["pizza", "size", "quantity", "notes"],
}


def read_menu_pizzas() -> list[str]:
    """Pizza names from menu.txt: the text before the first run of spaces."""
    lines = Path(__file__).with_name("menu.txt").read_text(encoding="utf-8").splitlines()
    return [line.split("  ")[0].strip() for line in lines[1:] if line.strip()]


MENU_PIZZAS = read_menu_pizzas()

SYSTEM_PROMPT = """You turn a customer's message into an order for Bella's Pizza.
Reply with JSON only: pizza (one pizza name), size (small, medium or large),
quantity (a whole number) and notes (extras such as "no olives", or "").
If the customer gives no size, use medium."""

EXAMPLES = [
    ("Three small pepperoni please", {"pizza": "Pepperoni", "size": "small", "quantity": 3, "notes": ""}),
    ("A large Hawaiian, extra cheese", {"pizza": "Hawaiian", "size": "large", "quantity": 1, "notes": "extra cheese"}),
]


def parse_order(message: str) -> Order:
    """Ask the model for an order as JSON, forced to match ORDER_SCHEMA."""
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for example_message, example_order in EXAMPLES:
        messages.append({"role": "user", "content": example_message})
        messages.append({"role": "assistant", "content": json.dumps(example_order)})
    messages.append({"role": "user", "content": message})
    reply = chat(messages, response_format=ORDER_SCHEMA)
    return Order(**json.loads(reply["content"]))


def validate_order(order: Order) -> list[str]:
    """Return a list of problems; an empty list means the order is fine."""
    problems = []
    if order.pizza not in MENU_PIZZAS:
        problems.append(f"'{order.pizza}' is not on the menu")
    if not 1 <= order.quantity <= 10:
        problems.append(f"quantity {order.quantity} is not between 1 and 10")
    return problems
