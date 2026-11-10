"""Talk to a language model running locally in Ollama."""

import json
import os
import urllib.request

OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:8b")


def ask_model(question: str, temperature: float = 0.0) -> str:
    """Send one question to the model and return its answer as text."""
    request_body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "stream": False,
        "think": False,
        "options": {"temperature": temperature},
    }
    request = urllib.request.Request(
        OLLAMA_BASE_URL + "/api/chat",
        data=json.dumps(request_body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        reply = json.load(response)
    return reply["message"]["content"]


def count_tokens(text: str) -> int:
    """Ask Ollama how many tokens the model sees in `text`.

    `raw` sends the text exactly as given, without the chat wrapping that
    ask_model() gets, and `num_predict` 1 stops the model after one token.
    """
    request_body = {
        "model": MODEL,
        "prompt": text,
        "raw": True,
        "stream": False,
        "options": {"num_predict": 1},
    }
    request = urllib.request.Request(
        OLLAMA_BASE_URL + "/api/generate",
        data=json.dumps(request_body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        reply = json.load(response)
    return reply["prompt_eval_count"]
