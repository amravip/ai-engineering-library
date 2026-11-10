"""Chapter 9: a chat history that trims itself to fit a token budget."""

from collections.abc import Callable


def estimate_tokens(text: str) -> int:
    """A rule of thumb: English averages about four characters per token.

    It is only an estimate. model.count_tokens() asks Ollama for the real
    number, but costs a round trip to the model each time.
    """
    return max(1, len(text) // 4)


def add_message(history: list[dict], role: str, content: str) -> None:
    """Append one turn to the history."""
    history.append({"role": role, "content": content})


def history_size(history: list[dict], count: Callable[[str], int]) -> int:
    """Total size of every message's text, measured with `count`."""
    return sum(count(message["content"]) for message in history)


def trim_history(
    history: list[dict], max_tokens: int, count: Callable[[str], int] = estimate_tokens
) -> list[dict]:
    """Return a copy that fits `max_tokens`, dropping the oldest turns first.

    System messages are never dropped: they hold the rules for the bot.
    """
    trimmed = list(history)
    while history_size(trimmed, count) > max_tokens:
        oldest = next((m for m in trimmed if m["role"] != "system"), None)
        if oldest is None:
            break
        trimmed.remove(oldest)
    return trimmed
