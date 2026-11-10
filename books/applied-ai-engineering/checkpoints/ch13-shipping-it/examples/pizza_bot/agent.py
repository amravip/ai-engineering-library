"""Chapter 12: the agent loop. Ask, run any tools the model requests, repeat."""

from model import chat
from shop_tools import TOOLS, run_tool

SYSTEM = ("You are the order assistant for Bella's Pizza. "
          "Use the tools for order details and for counting letters; never guess.")


def run_agent(question: str, max_steps: int = 5) -> str:
    """Answer `question`, letting the model call tools for up to `max_steps` rounds."""
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": question}]
    for _ in range(max_steps):
        reply = chat(messages, tools=TOOLS)
        messages.append(reply)
        if not reply.get("tool_calls"):
            return reply["content"]
        for call in reply["tool_calls"]:
            name = call["function"]["name"]
            arguments = call["function"]["arguments"]
            print(f"  model asked for {name}({arguments})")
            result = run_tool(name, arguments)
            print(f"  tool returned {result}")
            messages.append({"role": "tool", "content": result})
    return f"Sorry, I could not finish within {max_steps} steps."
