import requests

API_URL = "http://localhost:8080/completion"


def build_prompt(user_input: str) -> str:
    """
    Formats the user's input for the instruct model so that it can
    respond as a loyal gaurdian of King Arthur's castle.

    Below are prompt engineering tokens and their purpose...

    <|system|> = rules
    <|user|> = input
    <|assistant|> = obey + respond

    Args:
        user_input (str): Message the user wishes to say to the gaurd.

    Returns:
        str: Engineered prompt for native LLM
    """
    return f"""
        <|system|>
        You are a loyal servant of King Arthur.
        You guard the gate of Avalon.
        Respond in 1-2 sentences.
        Never break character.

        <|user|>
        {user_input}

        <|assistant|>
        """


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

    while (
        user_input := input(
            "\nRespond to the loyal servant of Aurthur "
            "(type 'exit' to quit): "
        )
    ).lower() != "exit":
        prompt = build_prompt(user_input)
        result = generate(prompt)
        print("\n" + result)


if __name__ == "__main__":
    main()
