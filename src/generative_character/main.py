import requests

from .prompt import build_instruct_prompt

API_URL = "http://localhost:8080/completion"


gaurd_rules = (
    "You are a loyal servant of King Arthur."
    "You guard the gate of Avalon."
    "Respond in 1-2 sentences."
    "Never break character."
)


def generate(prompt: str) -> str:
    """
    Sends prompt to native LLM for response.

    Args:
        prompt (str): Message for LLM to respond to.

    Returns:
        str: The native LLM's response.
    """
    try:
        response = requests.post(
            API_URL,
            json={"prompt": prompt},
            timeout=100,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("content", "").strip()

    except requests.exceptions.RequestException as e:
        return f"[Error communicating with LLM: {e}]"


def main():
    """
    Generative character program entrypoint run
    """
    while (
        user_input := input(
            "\nRespond to the loyal servant of Aurthur "
            "(type '/exit' to quit): "
        )
    ).lower() != "/exit":
        prompt = build_instruct_prompt(gaurd_rules, user_input)
        result = generate(prompt)
        print("\n" + result)


if __name__ == "__main__":
    main()
