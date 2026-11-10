"""Chapter 10: ask about something the model has never seen."""

from model import ask_model

question = "What time do you open on Sunday?"
role = "You answer customer questions for Bella's Pizza."
rule = "If you are not sure of the answer, say \"I don't know\"."

print("Customer:", question)
print("Bot (role only, no documents):", ask_model(f"{role}\n\nCustomer question: {question}"))
print()
print("Bot (told to say I don't know):", ask_model(f"{role} {rule}\n\nCustomer question: {question}"))
