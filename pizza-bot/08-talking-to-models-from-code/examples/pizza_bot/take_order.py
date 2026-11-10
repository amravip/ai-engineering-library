"""Parse three customer messages and check each order."""

from orders import parse_order, validate_order

messages = [
    "Two large margheritas, no olives",
    "Can I get a medium Hawaiian?",
    "One large Vegan Supreme please",
]

for message in messages:
    order = parse_order(message)
    print("Customer:", message)
    print("  Parsed:", order)
    print("  Problems:", validate_order(order) or "none")
