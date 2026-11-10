"""Tests for shop_tools.py and agent.py. They never call Ollama."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

import agent  # noqa: E402
import shop_tools  # noqa: E402


def tool_call(name, arguments):
    return {"role": "assistant", "content": "", "tool_calls": [
        {"function": {"name": name, "arguments": arguments}}]}


def answer(text):
    return {"role": "assistant", "content": text}


def test_orders_file_has_twenty_orders():
    assert [o["number"] for o in shop_tools.ORDERS] == list(range(1, 21))


def test_check_order_known_and_unknown():
    assert shop_tools.check_order(7)["number"] == 7
    assert "error" in shop_tools.check_order(99)


def test_count_letter():
    assert shop_tools.count_letter("mozzarella", "z") == 2
    assert shop_tools.count_letter("Margherita", "R") == 2


def test_run_tool_returns_json_and_handles_errors():
    assert json.loads(shop_tools.run_tool("count_letter", {"text": "pizza", "letter": "z"})) == 2
    assert "Unknown tool" in json.loads(shop_tools.run_tool("fly", {}))["error"]
    assert "error" in json.loads(shop_tools.run_tool("check_order", {"wrong": 1}))


def test_agent_runs_tool_then_answers(monkeypatch):
    replies = [tool_call("check_order", {"order_number": 7}), answer("It is out for delivery.")]
    sent = []

    def fake_chat(messages, **kwargs):
        sent.append(list(messages))
        assert kwargs["tools"] == shop_tools.TOOLS
        return replies.pop(0)

    monkeypatch.setattr(agent, "chat", fake_chat)
    assert agent.run_agent("Where is order 7?") == "It is out for delivery."
    second_call = sent[1]
    assert second_call[-1]["role"] == "tool" and "out for delivery" in second_call[-1]["content"]
    assert second_call[-2].get("tool_calls")


def test_agent_stops_after_max_steps(monkeypatch):
    calls = []

    def fake_chat(messages, **kwargs):
        calls.append(1)
        return tool_call("check_order", {"order_number": 1})

    monkeypatch.setattr(agent, "chat", fake_chat)
    result = agent.run_agent("loop forever", max_steps=3)
    assert len(calls) == 3
    assert "3 steps" in result


def test_agent_survives_unknown_tool(monkeypatch):
    replies = [tool_call("fly", {}), answer("Sorry, I cannot do that.")]
    monkeypatch.setattr(agent, "chat", lambda messages, **kwargs: replies.pop(0))
    assert agent.run_agent("fly me") == "Sorry, I cannot do that."
