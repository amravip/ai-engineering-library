"""Chapter 12: three questions that need tools."""

from agent import run_agent

questions = [
    "Where is my order #7?",
    "Is order #99 on its way?",
    "How many z's are in mozzarella?",
]

for question in questions:
    print("Customer:", question)
    print("Bot:", run_agent(question))
    print()
