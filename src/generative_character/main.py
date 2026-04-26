from .model import generate_text
from .grammar import load_grammar

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
        poignancy_response = generate_text(poignancy_rules, user_input, poignancy_grammar)
        print("\nPoignancy Rating: " + poignancy_response)

        gaurd_response = generate_text(gaurd_rules, user_input)
        print("\nGaurd Response: " + gaurd_response)


if __name__ == "__main__":
    main()

