# AI Engineering Examples: Build a Pizza Shop Assistant with Local Models

You build an assistant for a small pizza shop. It answers customer questions, reads orders, searches the shop's documents and checks its own answers. It runs on your own computer, with a local model.

The project has 13 steps. Each step adds one idea, and each step folder holds the complete code at that point.

## The steps

| Step | What you learn | Folder |
|---|---|---|
| 1 | Ask a local model a question, and give it the facts | [01-first-conversation](pizza-bot/01-first-conversation/README.md) |
| 2 | How a model reads text as tokens | [02-tokens](pizza-bot/02-tokens/README.md) |
| 3 | Embeddings: search by meaning | [03-embeddings](pizza-bot/03-embeddings/README.md) |
| 4 | Attention: each word looks at its neighbours | [04-attention](pizza-bot/04-attention/README.md) |
| 5 | Training a tiny model by counting | [05-training](pizza-bot/05-training/README.md) |
| 6 | Fine-tuning and the chat template | [06-fine-tuning](pizza-bot/06-fine-tuning/README.md) |
| 7 | Temperature: how varied the answers are | [07-temperature](pizza-bot/07-temperature/README.md) |
| 8 | Structured output, checked against the menu | [08-talking-to-models-from-code](pizza-bot/08-talking-to-models-from-code/README.md) |
| 9 | The context window, and what a model forgets | [09-the-context-window](pizza-bot/09-the-context-window/README.md) |
| 10 | Hallucination, and a checker for it | [10-hallucination](pizza-bot/10-hallucination/README.md) |
| 11 | Retrieval-augmented generation (RAG) | [11-rag](pizza-bot/11-rag/README.md) |
| 12 | Tools and agents | [12-tools-and-agents](pizza-bot/12-tools-and-agents/README.md) |
| 13 | Measuring quality, tokens and time | [13-shipping-it](pizza-bot/13-shipping-it/README.md) |

The [learning path](pizza-bot/README.md) describes each step in more detail. The [exercise for step 8](pizza-bot/exercises/08-structured-output/README.md) has code that you can test.

## Requirements

- Python 3.10 or newer. The code is tested on Python 3.13.
- [Ollama](https://ollama.com), running on your computer.
- The model `qwen3:8b`, which is about 5.2 GB. On a computer with 8 GB of memory, use `qwen3:1.7b` instead.
- The embedding model `nomic-embed-text` (274 MB), which you need from step 3.

```bash
ollama pull qwen3:8b
ollama pull nomic-embed-text
```

## Quick start

1. Get the code. Clone this repository, or choose **Code** and then **Download ZIP** on GitHub, and unzip it.
2. Open the first step's project folder.

   ```bash
   cd pizza-bot/01-first-conversation/examples/pizza_bot
   ```

3. Ask the model a question. Ollama must be running.

   ```bash
   python ask.py
   ```

The answer may name pizzas that are not on the menu. Step 1 explains why, and shows how to fix it.

## Configuration

The scripts read three environment variables. If you do not set them, the defaults below are used.

| Variable | Default | What it sets |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | The address of the Ollama server |
| `OLLAMA_MODEL` | `qwen3:8b` | The model for chat answers |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | The model for embeddings, from step 3 |

To use the smaller model, set the variable before you run a script.

```powershell
$env:OLLAMA_MODEL = "qwen3:1.7b"
```

```bash
export OLLAMA_MODEL=qwen3:1.7b
```

Your answers will differ from the saved outputs when you use a different model.

## Running the tests

The tests use fake models, so you do not need Ollama, the internet or a paid service. Install the test tool once, from the repository folder.

```bash
python -m pip install -r pizza-bot/requirements-dev.txt
```

Then run the tests in any step folder.

```bash
cd pizza-bot/13-shipping-it
python -m pytest -q
```

The result should be `50 passed`. Each later step includes the tests of the earlier steps.

## How the steps work

Each step folder is the complete project at the end of that step. You can work in two ways:

- Start from the step before. Copy its `examples/` and `tests/` folders, then follow the step's README.
- Open the step you need, and compare your files with it.

Each step README marks every file as New, Changed or Unchanged, so you can see what the step adds.

## Troubleshooting

**Connection refused.** The script stops with an error that includes `Connection refused`. On Windows, the message can read `No connection could be made because the target machine actively refused it`. Ollama is not running. Start the Ollama app, or run `ollama serve` in a terminal, and then run the script again. The tests do not need Ollama, so they still pass when it is stopped.

**Windows shows an error for the £ sign.** The script stops with `UnicodeEncodeError`. Tell Python to use UTF-8 for this terminal, and then run the script again.

```powershell
$env:PYTHONIOENCODING = "utf-8"
```

In Command Prompt, use `set PYTHONIOENCODING=utf-8`.

**The model is slow or runs out of memory.** Use the smaller model, as shown in the configuration section.

## Licence

The code is released under the [MIT Licence](LICENSE).
