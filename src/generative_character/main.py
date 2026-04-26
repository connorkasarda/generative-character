import requests

from .prompt import build_instruct_prompt

from llama_cpp import Llama, LlamaGrammar
from  pathlib import Path

API_URL = "http://localhost:8080/completion"

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
GRAMMARS_DIR = PROJECT_DIR / "grammars"

gaurd_rules = (
    "You are a loyal servant of King Arthur."
    "You guard the gate of Avalon."
    "Respond in 1-2 sentences as your character only."
    "Never break character."
)

poignancy_rules = (
    "You will rate the prompt by poignancy on a scale of 1 to 9."
    "1 is mundane and unimportant, 9 is very important and critical."
    "You will only return a number between 1 and 9 for poignancy rating."
)


def load_grammar(name):
    """
    Loads grammar rules from file to memory

    Args:
        name (str): Name of grammar file

    Returns:
        str: The grammar rules as a string
    """
    grammar_path = GRAMMARS_DIR / f"{name}.gbnf"

    with open(grammar_path, "r", encoding="utf-8") as grammar_file:
        return grammar_file.read()


def generate(prompt: str, grammar: str | None = None) -> str:
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
            API_URL,
            json=payload,
            timeout=100,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("content", "").strip()

    except requests.exceptions.RequestException as e:
        return f"[Error communicating with LLM: {e}]"


def get_model_response(rules: str, user_input: str, grammar: str | None = None) -> str:
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
    result = generate(prompt, grammar)
    return result


def main():
    """
    Generative character program entrypoint run
    """
    poignancy_grammar = load_grammar("rating")

    while (
        user_input := input(
            "\nRespond to the loyal servant of Aurthur "
            "(type '/exit' to quit): "
        )
    ).lower() != "/exit":
        poignancy_response = get_model_response(poignancy_rules, user_input, poignancy_grammar)
        print("\nPoignancy Rating: " + poignancy_response)

        gaurd_response = get_model_response(gaurd_rules, user_input)
        print("\nGaurd Response: " + gaurd_response)


if __name__ == "__main__":
    main()
