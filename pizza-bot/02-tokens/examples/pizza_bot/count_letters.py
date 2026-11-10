"""Ask the model to count letters, and check it with Python."""

from model import ask_model

questions = [
    ("r", "Margherita"),
    ("z", "mozzarella"),
    ("e", "pepperoni"),
    ("s", "Four Cheese, Mushroom, Hawaiian"),
]

for letter, text in questions:
    prompt = (f'How many times does the letter {letter} appear in "{text}"? '
              "Answer with just the number.")
    model_answer = ask_model(prompt).strip()
    true_answer = text.lower().count(letter)
    verdict = "right" if model_answer == str(true_answer) else "WRONG"
    print(f"{letter!r} in {text!r}: model says {model_answer}, "
          f"Python says {true_answer}  ({verdict})")
