"""Chapter 6: the same model with and without the chat template."""

from model import MODEL, chat, post_to_ollama

question = "What vegetarian pizzas do you have?"


def raw_continue(prompt: str) -> str:
    """Send text with no template: the model simply continues it."""
    reply = post_to_ollama("/api/generate", {
        "model": MODEL, "prompt": prompt, "raw": True, "stream": False,
        "options": {"temperature": 0.0, "num_predict": 60},
    })
    return reply["response"]


print("Raw, the bare question:")
print(raw_continue(question))
print()
print("Raw, the start of a document:")
print("Bella's Pizza menu\n\n" + raw_continue("Bella's Pizza menu\n\n"))
print()
print("Chat (template applied):")
print(chat([{"role": "user", "content": question}])["content"])
