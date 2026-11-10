# Development Standards

These standards apply to the code in `pizza-bot/`. They keep every step consistent, so a reader who has finished one step can read the code of the next.

## Python

- Python 3.10 or newer. The code is tested on Python 3.13, and CI also runs the tests on Python 3.10.
- Use the standard library first. `pizza-bot/requirements-dev.txt` holds the only test dependency, pytest.
- Add a framework only when a step teaches it. Until then, use plain functions, dictionaries and dataclasses.

## Models and configuration

- Ollama is the model runtime. The examples call Ollama's HTTP API on the local computer.
- Configuration comes from environment variables. There is no `.env` loader and no configuration framework.
- The variables are `OLLAMA_BASE_URL` (default `http://localhost:11434`), `OLLAMA_MODEL` (default `qwen3:8b`) and `OLLAMA_EMBED_MODEL` (default `nomic-embed-text`). Each is defined and defaulted in the step's `model.py`.
- A hosted provider may be offered as an option. It is never required to run the examples or the tests.

## Layout

```text
pizza-bot/
├── README.md                    the learning path
├── requirements-dev.txt         test dependencies
├── NN-<topic>/                  the complete project at the end of step NN
│   ├── README.md                what the step adds, the files, the commands, the expected results
│   ├── examples/                the project files; saved outputs in examples/expected/
│   └── tests/                   tests for the files in this step
└── exercises/
    └── NN-<topic>/
        ├── README.md            the exercises, and which ones need a live model
        ├── solutions/           code answers that can be tested
        └── tests/               tests for the solutions
```

Use names that describe the project's domain, such as `orders.py`, `check_order()` and `Order`, rather than abbreviations.

## Steps

- A step is the complete project at the end of that step, so a reader can stop after any step and resume from it.
- Each step README lists its files as New, Changed or Unchanged, and says how to check that earlier behaviour still works.
- A file that is unchanged from an earlier step is identical to it.

## Code style

- Small functions with meaningful names. Keep each function short enough to read on one screen.
- Type hints on every function signature.
- Explicit errors with messages a reader can act on.
- Comments explain why, not what. Docstrings are one or two sentences.
- Avoid unnecessary abstraction, deep inheritance and clever one-line expressions.
- Format and lint with ruff, using the rules in `ruff.toml`. Ruff runs in CI. Readers do not need it.

## Testing

- Unit tests use fakes. They never call a live model, the internet or a paid API.
- Fake the model by replacing the function that calls Ollama, for example `chat` or `urlopen`. Then check what was sent and how the reply is handled.
- Scripts that call a model are run by hand. Their saved outputs are real runs. Label them as real runs, record the model, the Ollama version and the date, and say that the wording will vary.
- Scripts that call no model must print the same text on every run, and the saved output must match it exactly. Label that output as fixed output.
- Regression tests keep earlier behaviour working when a later step changes a file.
- The CI workflow sets `OLLAMA_BASE_URL` to a closed port, so a test that reaches for a live model fails.

## Self-containment

- Each step prints everything a reader needs: the code, the configuration, the dependencies, the setup commands, the test code, the data and the expected output.
- Setup assumes only the tools a reader installs: Python, Ollama, Python packages and the model files.

## Wording

- Plain, friendly English with short sentences. Use British spelling.
- Say "step" for each part of the learning path.
- Keep the example's story simple and familiar: Bella's Pizza, a small pizza shop.

## What never goes in this repository

- Secrets, API keys and `.env` files.
- Model files and generated build output.

## Checks

Run these from the repository root:

```bash
python tools/check_repo.py
python -m ruff check pizza-bot tools
python -m compileall -q pizza-bot tools
cd pizza-bot/13-shipping-it && python -m pytest -q
cd ../exercises/08-structured-output && python -m pytest -q
```

GitHub Actions runs the same checks on Python 3.10 and 3.13, for every push and pull request. The workflow uses no secrets and calls no model.
