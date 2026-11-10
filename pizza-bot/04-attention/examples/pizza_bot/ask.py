"""Ask the model about Bella's menu, without showing it the menu."""

from model import ask_model

question = "What vegetarian pizzas do you have?"
print("Customer:", question)
print("Bot:", ask_model(question))
