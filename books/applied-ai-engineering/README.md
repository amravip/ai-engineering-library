# Applied AI Engineering

**Author:** Ravi Pal
**Primary project:** Pizza Store AI Assistant
**Industry:** Retail / Food
**Status:** In preparation. The code for all 13 chapters is available as checkpoints in this folder.

Applied AI Engineering builds one project from the first chapter to the last: an AI assistant for Bella's Pizza, a small pizza shop. Each chapter adds one idea to the same folder of Python files. You start with a single question to a local model and finish with a program that reads orders, searches the shop's documents and checks its own answers.

This folder contains the companion code for the book. The book is self-contained: every script, data file, test and expected output a chapter needs is printed in the book, and you do not need this repository to do the exercises. The code here is an optional convenience, so you can compare your files with a reference copy.

## What is here

| Path | What it holds |
|---|---|
| `checkpoints/ch01-first-conversation/` to `checkpoints/ch13-shipping-it/` | Thirteen checkpoints. Each one is the complete project at the end of its chapter: every script, data file, saved output and test up to that chapter. |
| `exercises/ch08/` | Chapter 8 exercise solutions that have a testable code answer, with their tests. |
| `requirements-dev.txt` | The test dependency, pytest. The book's code uses only the Python standard library. |

## Requirements

- **Python 3.10 or newer.** The book uses Python 3.13.
- **Ollama**, the local model runtime, running on your computer. Chapter 1 explains how to install it.
- **A local model.** The book's outputs come from `qwen3:8b`, which needs about 5.2 GB of disk space and a laptop with 16 GB of memory. On an 8 GB machine, use `qwen3:1.7b` (about 1.4 GB) instead. Every example still runs, but the answers are weaker.
- **An embedding model** from Chapter 3 onward: `nomic-embed-text` (274 MB).

```bash
ollama pull qwen3:8b
ollama pull nomic-embed-text
```

The scripts need Ollama running to call a model. The tests and the scripts that print fixed output do not.

## Configuration

Configuration is read from environment variables. There is no configuration file and no `.env` loader.

| Variable | Default | Used for |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | The address where Ollama is listening. |
| `OLLAMA_MODEL` | `qwen3:8b` | The chat model. Set it to `qwen3:1.7b` if you downloaded the smaller model. |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | The model that turns text into embeddings. |

The values are read in `model.py`. Setting one of them in your shell changes it for every script:

```bash
export OLLAMA_MODEL=qwen3:1.7b        # macOS or Linux
set OLLAMA_MODEL=qwen3:1.7b           # Windows Command Prompt
$env:OLLAMA_MODEL = "qwen3:1.7b"      # Windows PowerShell
```

No hosted provider is needed. The book's core examples run on Ollama alone.

## Get the code

Clone the repository, or download it as a ZIP file from the GitHub "Code" button, and then open the first checkpoint:

```bash
git clone https://github.com/amravip/ai-engineering-library.git
cd ai-engineering-library
cd books/applied-ai-engineering/checkpoints/ch01-first-conversation
```

If you downloaded the ZIP file instead, unzip it and run the last `cd` command from the folder that holds `books/`.

## How checkpoints work

A checkpoint is the complete project at the end of one chapter. You can stop after any chapter, and you can start a later chapter from its checkpoint.

Each checkpoint folder has the same parts:

- `README.md`: a step-by-step guide to the chapter. It lists the files that are new or changed, the commands to run, and the expected results.
- `examples/`: the project. Scripts live in `examples/pizza_bot/`, and the saved outputs live in `examples/expected/`.
- `tests/`: the tests for the files in that checkpoint.

The scripts run from inside `examples/pizza_bot/`, and the tests find that folder themselves. You can run the tests from anywhere that has the checkpoint folder.

Saved outputs come in two kinds, and each checkpoint README says which is which:

- **Fixed output.** Scripts that do not call a model print the same text on every run. Running them again should match the saved file exactly.
- **Real runs.** Scripts that call a model print different wording on different machines and on different days. The saved file records one real run, and your output will differ.

## Step-by-step guide

Each row links to the guide for that chapter. Start with Chapter 1, or start at any chapter from the checkpoint before it.

| Chapter | What you build | Guide |
|---|---|---|
| 1. Your First Conversation with a Model | Ask a local model a question, then give it Bella's menu so that it answers from the facts. | [README](checkpoints/ch01-first-conversation/README.md) |
| 2. Tokens | A small tokenizer that learns word pieces, and a count of the real tokens a model sees. | [README](checkpoints/ch02-tokens/README.md) |
| 3. Embeddings | A search that finds menu lines by meaning, using an embedding model. | [README](checkpoints/ch03-embeddings/README.md) |
| 4. Attention | Attention in plain Python, and a look at how "hot" changes meaning from one sentence to the next. | [README](checkpoints/ch04-attention/README.md) |
| 5. Training | A next-word model that learns by counting, and a loss that falls during training. | [README](checkpoints/ch05-training/README.md) |
| 6. Fine-tuning | A `chat()` function, the chat template, and a toy model taught to answer with question-and-answer pairs. | [README](checkpoints/ch06-fine-tuning/README.md) |
| 7. Temperature | Temperature on a counting model and on the real model, with a seed. | [README](checkpoints/ch07-temperature/README.md) |
| 8. Talking to Models from Code | A customer's sentence turned into an `Order`, and checked against the menu. | [README](checkpoints/ch08-talking-to-models-from-code/README.md) |
| 9. The Context Window | A chat that forgets, and the same chat fixed by trimming its history and keeping a summary. | [README](checkpoints/ch09-the-context-window/README.md) |
| 10. Hallucination | A check that flags pizza names that are not on the menu. | [README](checkpoints/ch10-hallucination/README.md) |
| 11. Retrieval-Augmented Generation | Answers from Bella's shop documents, with the file name cited. | [README](checkpoints/ch11-rag/README.md) |
| 12. Tools and Agents | Tools that look up an order and count letters, and a loop that uses them. | [README](checkpoints/ch12-tools-and-agents/README.md) |
| 13. Shipping It: From Demo to Product | An eval of ten questions, and a measure of tokens and seconds. | [README](checkpoints/ch13-shipping-it/README.md) |

## Running the tests

The tests use fake models. They never call Ollama, the internet or a paid service, so they pass without a model installed.

```bash
cd books/applied-ai-engineering
python -m pip install -r requirements-dev.txt

cd checkpoints/ch13-shipping-it
python -m pytest -q
```

The Chapter 13 checkpoint has all 50 tests. Each earlier checkpoint runs the tests for the chapters up to it, and its README gives the count. The exercise solutions have their own tests:

```bash
cd books/applied-ai-engineering/exercises/ch08
python -m pytest -q
```

The exercise notes for Chapter 8 are in [`exercises/ch08`](exercises/ch08/README.md).
