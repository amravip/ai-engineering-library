"""Answer a question from retrieved documents, and cite them."""

from model import ask_model
from search import embedding_search


def answer_with_sources(question: str, documents: dict[str, str], top: int = 2) -> str:
    """Retrieve the best documents, paste them into the prompt, and ask."""
    best = embedding_search(question, documents, top)
    labelled = "\n\n".join(f"[{name}]\n{documents[name]}" for name, _ in best)
    prompt = f"""You answer customer questions for Bella's Pizza.
Use only the documents below. If they do not contain the answer, say you don't know.
End your answer with the file name of each document you used, in brackets.

{labelled}

Customer question: {question}"""
    return ask_model(prompt)
