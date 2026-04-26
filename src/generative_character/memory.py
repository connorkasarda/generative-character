import time


class Memory:
    """
    Encapsulates a recorded unit of the character's experiences
    """

    def __init__(self, description: str):
        self.description = description
        self.timestamp = int(time.time())
