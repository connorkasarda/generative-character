import requests

from .prompt import build_instruct_prompt

LLM_API_URL = "http://localhost:8080/completion"

def get_model_http_response(prompt: str, grammar: str | None = None) -> str:
    """
    Sends prompt to native LLM for response.

    Args:
        prompt (str): Message for LLM to respond to.
        grammar (str): The grammar rules

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
            LLM_API_URL,
            json=payload,
            timeout=100,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("content", "").strip()

    except requests.exceptions.RequestException as e:
        return f"[Error communicating with LLM: {e}]"


def generate_text(rules: str, user_input: str, grammar: str | None = None) -> str:
    """
    Retrieves model response

    Args:
        rules (str): Instructions for model to follow
        grammar (str): Restriction to models token output
        user_input (str): What the user asked the model

    Returns:
        str: Result of the model's response
    """
    prompt = build_instruct_prompt(rules, user_input)
    result = get_model_http_response(prompt, grammar)
    return result

