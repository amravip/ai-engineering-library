"""Does the real model pick the right meaning of "hot"?"""

from model import ask_model

contexts = [
    "The BBQ Chicken has chilli on it. Is the BBQ Chicken hot?",
    "My pizza arrived an hour late. Is the pizza hot?",
]

for message in contexts:
    prompt = (f'A customer writes: "{message}"\n'
              'In one short sentence, what does "hot" mean here?')
    print("Customer:", message)
    print("Model:", ask_model(prompt))
    print()
