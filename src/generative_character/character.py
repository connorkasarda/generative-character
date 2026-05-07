import json

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
        self.rules = rules
        self.grammar = load_grammar("character")

    def interact(self, user_input: str) -> str:
        """
        Computes a respond/reflect cycle when given
        exterior dialogue (e.g., text from the player).

        Args:
            user_input (str): Player's request

        Returns:
            str: Character's final response
        """
        response = generate_text(self.rules, user_input, self.grammar)
        json_data = json.loads(response)

        response = json_data["response"]
        poignancy = json_data["poignancy"]
        description = json_data["description"]

        self.memories.append(Memory(description, poignancy))

        return response
