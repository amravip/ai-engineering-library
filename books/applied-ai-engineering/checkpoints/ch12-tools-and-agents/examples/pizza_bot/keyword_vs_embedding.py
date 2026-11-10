"""Chapter 11: keyword search against embedding search on the same questions."""

from pathlib import Path

from search import embedding_search, keyword_search, load_documents

documents = load_documents(Path(__file__).with_name("shop_docs"))

questions = [
    "Is there a coeliac-friendly option?",
    "What if my food shows up freezing?",
    "Can I use a coupon?",
    "When are you open on Sunday?",
]

for question in questions:
    print("Question:", question)
    print("  keywords :", [(name, score) for name, score in keyword_search(question, documents)])
    print("  embedding:", [(name, round(score, 3)) for name, score in embedding_search(question, documents)])
