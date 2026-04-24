import requests

from .prompt import build_instruct_prompt

API_URL = "http://localhost:8080/completion"


gaurd_rules = (
    "You are a loyal servant of King Arthur."
    "You guard the gate of Avalon."
    "Respond in 1-2 sentences."
    "Never break character."
)

poingancy_rater_rules = ()

# TODO Define a GBNF that restricts the LLM output for poignancy rating


def generate(prompt: str, grammar: str | None = None) -> str:
    """
    Sends prompt to native LLM for response.

    Args:
        prompt (str): Message for LLM to respond to.

    Returns:
        str: The native LLM's response.
    """
    try:
        payload = {
            "prompt": prompt,
        }

        if grammar is not None:
            payload["grammar"] = grammar

        response = requests.post(
            API_URL,
            json=payload,
            timeout=100,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("content", "").strip()

    except requests.exceptions.RequestException as e:
        return f"[Error communicating with LLM: {e}]"


def get_model_response(rules: str, input: str) -> str:
    """ """
    prompt = build_instruct_prompt(rules, input)
    result = generate(prompt)
    return result


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
        gaurd_response = get_model_response(gaurd_rules, user_input)
        print("\nGaurd Response: " + gaurd_response)


if __name__ == "__main__":
    main()
