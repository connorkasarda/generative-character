from .grammar import load_grammar
from .memory import Memory
from .model import generate_text


class Character:
    """
    LLM wrapper that adds memory and reasoning logic
    for the production of character dialogue.
    """

    def __init__(self, rules: str, init_memories: list[Memory] | None = []):
        """
        Args:
            rules (str):
                Literal containing character rules that are fed to instruct LLM
            init_memories (list[Memory]):
                If available, add initial memories on character spawn
        """
        self.memories = init_memories

        self.character_rules = rules
        self.poignancy_rules = (
            "You will rate the interaction by poignancy on a scale of 1 to 9."
            "1 is mundane and unimportant, 9 is very important and critical."
            "Only return a number between 1 and 9 for poignancy rating."
        )
        self.historian_rules = (
            "Describe the interaction between the player and the character."
            "Only reflect on implications of the interaction."
            "Respond in 1-3 sentences only."
        )

        self.poignancy_grammar = load_grammar("rating")

    def respond(self, user_input: str) -> str:
        """
        Generates response to user's prompt that abides to character's style

        Args:
            user_input (str): Player's request

        Returns:
            str: Response from LLM that follows style of character
        """
        # TODO Utilize memories to inform character's response
        return generate_text(self.character_rules, user_input)

    def reflect(self, user_input: str, character_response: str) -> None:
        """
        Stores result of user's prompt and character's reaction into memory.

        Args:
            user_input (str): Player's request
            character_response (str): Character's generated response

        Returns:
            None
        """
        interaction = (
            f"player: {user_input}\n"
            f"character: {character_response}"
        )

        description = generate_text(self.historian_rules, interaction)
        poignancy = generate_text(self.poignancy_rules, interaction, self.poignancy_grammar)

        new_memory = Memory(description, poignancy)
        self.memories.append(new_memory)

        # TODO Only for debug purposes
        print(f"New Memory!\n\tDescription: {new_memory.description}\n\tPoignancy: {new_memory.poignancy_rating}")

    def interact(self, user_input: str) -> str:
        """
        Computes a respond/reflect cycle when given
        exterior dialogue (e.g., text from the player).

        Args:
            user_input (str): Player's request

        Returns:
            str: Character's final response
        """
        character_response = self.respond(user_input)
        self.reflect(user_input, character_response)

        return character_response
