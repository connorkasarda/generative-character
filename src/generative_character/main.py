from .character import Character

gaurd_rules = (
    "You are a royal guard."
    "Respond in character,"
    "then rate the poignancy of the interaction from 1-10,"
    "and finally describe the interaction between "
    "the player (user) and the character (you)."
    "Character response should be 1-2 sentences."
    "For poignancy, 1 is unimportant and 10 is very important."
    "Description should regard user input"
    "and character response and be 1-2 sentences."
    "Return JSON in this format:"
    '{ "response": string, "poignancy": number, "description": string }'
)


def main():
    """
    Generative character program entrypoint run
    """

    gaurd_character = Character(gaurd_rules)

    while (
        user_input := input(
            "\nRespond to the loyal servant of Aurthur "
            "(type '/exit' to quit): "
        )
    ).lower() != "/exit":
        gaurd_response = gaurd_character.interact(user_input)
        print(f'\n"{gaurd_response}" - Gaurd')


if __name__ == "__main__":
    main()
