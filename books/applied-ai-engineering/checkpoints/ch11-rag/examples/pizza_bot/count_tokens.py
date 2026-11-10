"""Chapter 2: how many tokens does the real model see?"""

from pathlib import Path

from model import MODEL, count_tokens

print("Model:", MODEL)
for text in ["pizza", "Margherita", "mozzarella", "Pepperoni pizza",
             "What vegetarian pizzas do you have?"]:
    print(f"{count_tokens(text):3} tokens  {text!r}")

menu = Path(__file__).with_name("menu.txt").read_text(encoding="utf-8")
print()
print("Bella's menu:")
print(f"  {len(menu):4} characters")
print(f"  {len(menu.split()):4} words")
print(f"  {count_tokens(menu):4} tokens")
