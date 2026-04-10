def build_instruct_prompt(rules: str, input: str) -> str:
    """
    Formats the user's input for the instruct model.

    Below are key tokens for an instruct model...

    <|system|> = rules
    <|user|> = input
    <|assistant|> = obey + respond

    Args:
        rules (str): Instructions for the language model to obey in response.
        input (str): Message the user wishes to say to the generative character.

    Returns:
        str: Prompt properly formatted for the native instruct model
    """
    return f"""
        <|system|>
        {rules}

        <|user|>
        {input}

        <|assistant|>
        """
