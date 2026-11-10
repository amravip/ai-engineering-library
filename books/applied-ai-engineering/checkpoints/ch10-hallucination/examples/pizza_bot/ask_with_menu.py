"""Chapter 1: the same question, with Bella's real menu pasted into the prompt."""

from pathlib import Path

from model import ask_model

menu = Path(__file__).with_name("menu.txt").read_text(encoding="utf-8")
question = "What vegetarian pizzas do you have?"

prompt = f"""You answer customer questions for Bella's Pizza.
Use only the menu below. If the answer is not in the menu, say you don't know.

{menu}
Customer question: {question}"""

print("Customer:", question)
print("Bot:", ask_model(prompt))
