# Step 5: Training

This step builds the smallest language model that can learn. It learns by counting which word follows which, using Bella's customer reviews. You watch the loss fall as it trains. The loss is a score for how surprised the model is by the right next word. Lower is better.

## Before you start

- Start from the step 4 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 4.
- The training script does not need Ollama. The `ask_with_menu.py` check at the end does need Ollama and `qwen3:8b`.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/next_word.py` | A next-word model that learns by counting. It has the training, probability and generation functions. Key idea: training is only counting which word follows which, and then turning those counts into probabilities. |
| New | `examples/pizza_bot/train_next_word.py` | Trains the model, generates text and measures the loss. Key idea: the loss tells you how well the model predicts, and it falls as the counts grow. |
| New | `examples/expected/train_next_word.txt` | Saved output of the training script. Key idea: compare the loss numbers to see the fall. |
| Changed | `tests/test_inside_the_model.py` | Five tests for the counting model are added to the four from step 4. Key idea: each test checks one rule of the counting model. |

Unchanged: `model.py`, `reviews.txt` (used as training text), `tokenizer.py`, `attention.py` and the step 1 files.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Train the next-word model. This step does not need a model.

   ```bash
   python train_next_word.py
   ```

   The output should say "Words the model knows: 97". The greedy text should begin "the margherita was perfect". The held-out loss should fall from 4.70 to 3.47.
   Saved output: `examples/expected/train_next_word.txt`. **Fixed output (should match exactly).**

3. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `17 passed`. The tests do not need Ollama.

## What you learned

- A simple model can learn word patterns just by counting.
- The loss is a number you can watch while a model trains.
- Always choosing the most likely next word can make the text loop.

## Next

Go to [Step 6: Fine-tuning](../06-fine-tuning/README.md).
