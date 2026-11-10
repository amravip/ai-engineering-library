"""Flag invented pizzas in the two saved answers from ask.py and ask_with_menu.py."""

from pathlib import Path

from grounding import unsupported_pizzas

here = Path(__file__).parent
menu = (here / "menu.txt").read_text(encoding="utf-8")

for name in ["ask.txt", "ask_with_menu.txt"]:
    answer = (here / ".." / "expected" / name).read_text(encoding="utf-8")
    print(f"{name}: not on the menu -> {unsupported_pizzas(answer, menu) or 'nothing flagged'}")
