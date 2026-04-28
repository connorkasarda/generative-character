from .memory import Memory
from .model import generate_text

class Character:
    """
    LLM wrapper that adds memory and reasoning logic
    for the production of character dialogue.
    """

    def __init__(self, role: str, init_memories: list[Memory] | None = []):
        """ """
        self.memories = init_memories
        self.role = role
