"""Chapter 13: what one call costs in tokens and seconds."""

import time

from model import MODEL, post_to_ollama

questions = [
    "Hi!",
    "What vegetarian pizzas do you have? Answer in one sentence.",
    "Explain in detail how to make a pizza dough from scratch.",
]

for question in questions:
    started = time.time()
    reply = post_to_ollama("/api/chat", {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "stream": False,
        "think": False,
        "options": {"temperature": 0.0},
    })
    seconds = time.time() - started
    print(f"{question!r}: {reply['prompt_eval_count']} tokens in, "
          f"{reply['eval_count']} tokens out, {seconds:.1f} s "
          f"(Ollama total_duration {reply['total_duration'] / 1e9:.1f} s)")
