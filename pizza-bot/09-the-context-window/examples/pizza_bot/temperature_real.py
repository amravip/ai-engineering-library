"""Temperature with the real model."""

from model import chat

NAME = "Invent a name for Bella's new pizza. Reply with the name only."
SUM = "Add up: 2 Margheritas at £9 and 1 Pepperoni at £11. Reply with the total only."


def reply(prompt: str, temperature: float, options: dict | None = None) -> str:
    return chat([{"role": "user", "content": prompt}], temperature, options=options)["content"].strip()


for temperature in [0.0, 1.2]:
    print(f"Name, temperature {temperature}:")
    for _ in range(3):
        print("  ", reply(NAME, temperature))

for temperature in [0.0, 1.2]:
    print(f"Total, temperature {temperature}:", reply(SUM, temperature))

print("Name, temperature 1.2, seed 1, twice:")
for _ in range(2):
    print("  ", reply(NAME, 1.2, {"seed": 1}))
