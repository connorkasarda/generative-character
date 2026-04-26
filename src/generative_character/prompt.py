def build_instruct_prompt(rules: str, user_input: str) -> str:
    """
    Formats the user's input for the instruct model.

    Args:
        rules (str): Instructions for the language model to obey in response.
        user_input (str): Message the user wishes to say to the generative character.

    Returns:
        str: Prompt properly formatted for the native instruct model
    """
    return f"""<s>[INST]
        {rules}

        Input: {user_input}

        Output:
        [/INST]"""
