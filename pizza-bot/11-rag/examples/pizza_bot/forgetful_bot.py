"""A long chat in a tiny context window, and what the model forgets."""

from chat_script import CHATTY_TURNS, EARLY_TURNS, QUESTION, SYSTEM
from conversation import add_message
from model import MODEL, post_to_ollama

history = [{"role": "system", "content": SYSTEM}]
for role, content in EARLY_TURNS + CHATTY_TURNS:
    add_message(history, role, content)
add_message(history, "user", QUESTION)

reply = post_to_ollama("/api/chat", {
    "model": MODEL,
    "messages": history,
    "stream": False,
    "think": False,
    "options": {"temperature": 0.0, "num_ctx": 256},
})

print("Customer:", QUESTION)
print("Bot:", reply["message"]["content"])
print("Tokens the model actually read (prompt_eval_count):", reply["prompt_eval_count"])
