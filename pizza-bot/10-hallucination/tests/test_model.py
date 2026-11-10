"""Unit tests for ask_model(). They never call Ollama."""

import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

import model  # noqa: E402


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def test_ask_model_sends_question_and_returns_answer(monkeypatch):
    sent = {}

    def fake_urlopen(request, timeout):
        sent["url"] = request.full_url
        sent["body"] = json.loads(request.data)
        reply = {"message": {"role": "assistant", "content": "We have a Margherita."}}
        return FakeResponse(json.dumps(reply).encode("utf-8"))

    monkeypatch.setattr(model.urllib.request, "urlopen", fake_urlopen)

    answer = model.ask_model("What vegetarian pizzas do you have?")

    assert answer == "We have a Margherita."
    assert sent["url"].endswith("/api/chat")
    assert sent["body"]["messages"] == [
        {"role": "user", "content": "What vegetarian pizzas do you have?"}
    ]
    assert sent["body"]["stream"] is False
    assert sent["body"]["options"]["temperature"] == 0.0


def test_menu_has_four_vegetarian_pizzas():
    menu = (Path(model.__file__).with_name("menu.txt")).read_text(encoding="utf-8")
    vegetarian = [line for line in menu.splitlines() if "vegetarian" in line]
    assert len(vegetarian) == 4
