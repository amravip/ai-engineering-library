# Chapter 5: Training

This chapter builds the smallest language model that can learn. It learns by counting which word follows which, using Bella's customer reviews. You watch the loss fall as it trains.

## Before you start

- Start from the checkpoint `ch04-attention`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 4.
- The training script does not need Ollama. The `ask_with_menu.py` check at the end does need Ollama and `qwen3:8b`.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/next_word.py` | A next-word model that learns by counting. It has the training, probability and generation functions. | 5.1, 5.2, 5.4 |
| New | `examples/pizza_bot/train_next_word.py` | Trains the model, generates text and measures the loss. | 5.3 |
| New | `examples/expected/train_next_word.txt` | Saved output of the training script. | Output 5.1 |
| Changed | `tests/test_inside_the_model.py` | Five tests for the counting model are added to the four from Chapter 4. | Not printed in the chapter |

Unchanged: `model.py`, `reviews.txt` (used as training text), `tokenizer.py`, `attention.py` and the Chapter 1 files.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Train the next-word model. This step does not need a model.

   ```bash
   python train_next_word.py
   ```

   The output should say "Words the model knows: 97". The greedy text should begin "the margherita was perfect". The held-out loss should fall from 4.70 to 3.47.
   Saved output: `examples/expected/train_next_word.txt`. **Fixed output (should match exactly).**

3. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

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

Go to [Chapter 6: Fine-tuning](../ch06-fine-tuning/README.md), in the checkpoint `ch06-fine-tuning`.
