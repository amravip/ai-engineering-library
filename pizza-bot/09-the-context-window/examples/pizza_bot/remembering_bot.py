"""The same chat, but a short summary lives in the system message."""

from chat_script import CHATTY_TURNS, EARLY_TURNS, QUESTION, SYSTEM
from conversation import add_message, trim_history
from model import MODEL, post_to_ollama

SUMMARY = "Customer: Priya. Order so far: two large Pepperoni pizzas."
BUDGET = 150  # estimated tokens for the whole history; the window is 256

history = [{"role": "system", "content": SYSTEM + "\n" + SUMMARY}]
for role, content in EARLY_TURNS + CHATTY_TURNS:
    add_message(history, role, content)
add_message(history, "user", QUESTION)

trimmed = trim_history(history, BUDGET)
print(f"Kept {len(trimmed)} of {len(history)} messages.")

reply = post_to_ollama("/api/chat", {
    "model": MODEL,
    "messages": trimmed,
    "stream": False,
    "think": False,
    "options": {"temperature": 0.0, "num_ctx": 256},
})

print("Customer:", QUESTION)
print("Bot:", reply["message"]["content"])
print("Tokens the model actually read (prompt_eval_count):", reply["prompt_eval_count"])
