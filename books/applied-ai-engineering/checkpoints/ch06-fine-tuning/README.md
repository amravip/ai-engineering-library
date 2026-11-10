# Chapter 6: Fine-tuning

This chapter explains why a model that continues text does not answer questions. It adds `chat()` to `model.py`, which sends a list of messages. It shows the chat template that Ollama builds around each message. It also teaches the small model to answer with a set of question-and-answer pairs.

## Before you start

- Start from the checkpoint `ch05-training`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 5.
- You need Ollama running with `qwen3:8b`. One script in this step does not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/qa_pairs.txt` | Twelve question-and-answer pairs about the menu. | 6.3 |
| New | `examples/pizza_bot/fine_tune_demo.py` | The toy model, with and without the question-and-answer pairs. | 6.4 |
| New | `examples/pizza_bot/raw_vs_chat.py` | The same question sent in raw mode and through `chat()`. | 6.2 |
| New | `examples/pizza_bot/show_template.py` | Prints the chat template and the text the model receives. | 6.5 |
| Changed | `examples/pizza_bot/model.py` | Adds `chat()`, which sends a whole list of messages and returns the reply. | 6.1 |
| New | `examples/expected/fine_tune_demo.txt`, `raw_vs_chat.txt` and `show_template.txt` | Saved outputs of the three scripts above. | Output 6.1 to 6.5 |

Unchanged: `reviews.txt`, `next_word.py`, `train_next_word.py`, `tokenizer.py`, `ask.py`, `ask_with_menu.py` and `menu.txt`.

No new test file is added in this chapter. The tests from Chapter 5 still run.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the fine-tuning demo. This step does not need a model.

   ```bash
   python fine_tune_demo.py
   ```

   The reviews-only model should print "(nothing)". The tuned model should continue with text that begins "the margherita is".
   Saved output: `examples/expected/fine_tune_demo.txt`. **Fixed output (should match exactly).**

3. Show the chat template. This step needs Ollama and `qwen3:8b`.

   ```bash
   python show_template.py
   ```

   The output should say "first 25 of 64 lines" for `qwen3:8b`, followed by text that starts with `<|im_start|>user`. A different Ollama version may count the lines differently.
   Saved output: `examples/expected/show_template.txt`. **Real run (your wording will differ).**

4. Compare raw mode with chat mode. This step needs Ollama and `qwen3:8b`.

   ```bash
   python raw_vs_chat.py
   ```

   The first run can take about a minute while the model loads. In raw mode, the model should continue the question rather than answer it. The chat reply should read as an answer.
   Saved output: `examples/expected/raw_vs_chat.txt`. **Real run (your wording will differ).**

5. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `17 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 7: Temperature](../ch07-temperature/README.md), in the checkpoint `ch07-temperature`.
