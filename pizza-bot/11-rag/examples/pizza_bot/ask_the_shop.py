"""Four customer questions, answered from the shop documents."""

from pathlib import Path

from rag import answer_with_sources
from search import load_documents

documents = load_documents(Path(__file__).with_name("shop_docs"))

questions = [
    "What time do you open on Sunday?",
    "Is anything on the menu safe for someone with a nut allergy?",
    "My pizza came 45 minutes late. Can I get a refund?",
    "Do you have a gluten-free base?",
]

for question in questions:
    print("Customer:", question)
    print("Bot:", answer_with_sources(question, documents))
    print()
