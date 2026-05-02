from .character import Character

gaurd_rules = (
    "You are a loyal servant of King Arthur."
    "You guard the gate of Avalon."
    "Respond in 1-2 sentences as your character only."
    "Never break character."
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
        print('\n"' + gaurd_response + '" - Guard')


if __name__ == "__main__":
    main()
