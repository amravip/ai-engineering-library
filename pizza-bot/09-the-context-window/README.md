# Step 9: The Context Window

A customer chats with the bot for ten minutes, then asks, "What did I order?" The bot answers with complete confidence, and it gets the name wrong. A model sees only the text that fits in its context window, and a chatbot's memory is just the messages you resend. This step reproduces that failure on purpose. Then it fixes the failure in two ways: by trimming the history, and by keeping a short summary.

## Before you start

- Start from the step 8 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 8.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/conversation.py` | `add_message()`, `estimate_tokens()` and `trim_history()`. Key idea: the model's memory is the list of messages you send, so trimming that list changes what the model knows. |
| New | `examples/pizza_bot/chat_script.py` | The scripted chat that both bots in this step share. Key idea: both bots get the same messages, so the only difference is how each one keeps its history. |
| New | `examples/pizza_bot/forgetful_bot.py` | A long chat with no trimming. Key idea: when the chat grows past the window, the early facts fall out of view. |
| New | `examples/pizza_bot/remembering_bot.py` | A trimmed history, plus a summary. Key idea: a short summary keeps the important facts after the old messages are removed. |
| New | `examples/expected/forgetful_bot.txt` and `remembering_bot.txt` | Saved outputs of the two bots. Key idea: compare how each bot handles the name. |
| New | `tests/test_conversation.py` | Five tests of the trimming functions. Key idea: the system message is always kept, and the oldest turns are dropped first. |

Unchanged: `model.py`, `menu.txt` and the step 1 files.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the bot that forgets. This step needs Ollama and `qwen3:8b`.

   ```bash
   python forgetful_bot.py
   ```

   The bot should print a wrong or invented name instead of Priya. The `prompt_eval_count` should be below 256. The exact wording and count will differ on your machine.
   Saved output: `examples/expected/forgetful_bot.txt`. **Real run (your wording will differ).**

3. Run the bot that trims its history. This step needs Ollama and `qwen3:8b`.

   ```bash
   python remembering_bot.py
   ```

   The script prints `Kept 9 of 16 messages.` on every run, because trimming does not use a model.
   Saved output: `examples/expected/remembering_bot.txt`. **Real run (your wording will differ).**

4. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `29 passed`. The tests do not need Ollama.

## What you learned

- A chat model has no memory of its own. It sees only the messages you send with each request.
- A long history can push early facts out of the window.
- Trimming and summarising are two ways to keep the facts that matter.

## Next

Go to [Step 10: Hallucination](../10-hallucination/README.md).
