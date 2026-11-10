"""Tests for evaluate.py's grading and routing. They never call Ollama."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

import evaluate  # noqa: E402


def test_grade_requires_every_included_word_ignoring_case():
    check = {"must_include": ["Margherita", "£9"]}
    assert evaluate.grade("The margherita costs £9.", check)
    assert not evaluate.grade("The margherita is lovely.", check)


def test_grade_fails_on_banned_word():
    check = {"must_include": ["menu"], "must_not_include": ["Hawaiian"]}
    assert evaluate.grade("Our menu is short.", check)
    assert not evaluate.grade("Our menu has a Hawaiian.", check)


def test_grade_with_no_rules_passes():
    assert evaluate.grade("anything", {})


def test_eval_questions_file_is_well_formed():
    path = Path(evaluate.__file__).with_name("eval_questions.json")
    checks = json.loads(path.read_text(encoding="utf-8"))
    assert len(checks) == 10
    assert all(c["question"] and c.get("must_include") for c in checks)


def test_order_questions_go_to_agent_and_others_to_rag(monkeypatch):
    monkeypatch.setattr(evaluate, "run_agent", lambda question: "agent")
    monkeypatch.setattr(evaluate, "answer_with_sources", lambda question, documents: "rag")
    assert evaluate.answer_question("Where is order #7?", {}) == "agent"
    assert evaluate.answer_question("When do you open?", {}) == "rag"
