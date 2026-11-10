# Chapter 9: The Context Window

This chapter reproduces a failure that happens in a long chat. The bot forgets what a customer said early on, and it can call the customer by a name she never gave. Then you fix it in two ways: by trimming the history, and by keeping a summary.

## Before you start

- Start from the checkpoint `ch08-talking-to-models-from-code`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 8.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/conversation.py` | `add_message()`, `estimate_tokens()` and `trim_history()`. | 9.1, 9.4, 9.5 |
| New | `examples/pizza_bot/chat_script.py` | The scripted chat that both bots in this chapter share. | 9.2 |
| New | `examples/pizza_bot/forgetful_bot.py` | A long chat with no trimming. | 9.3 |
| New | `examples/pizza_bot/remembering_bot.py` | A trimmed history, plus a summary. | 9.6 |
| New | `examples/expected/forgetful_bot.txt` and `remembering_bot.txt` | Saved outputs of the two bots. | Output 9.1 and 9.2 |
| New | `tests/test_conversation.py` | Five tests of the trimming functions. They use a word counter and no model. | Not printed in the chapter |

Unchanged: `model.py`, `menu.txt` and the Chapter 1 files.

## Steps

1. From the checkpoint folder, open the project folder.

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

4. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `29 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 10: Hallucination](../ch10-hallucination/README.md), in the checkpoint `ch10-hallucination`.
