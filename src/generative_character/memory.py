import time
import numpy as np

class Memory:
    """
    Encapsulates a recorded unit of the character's experiences
    """

    def __init__(
            self,
            id: int,
            player_message: str,
            character_response: str,
            description: str,
            embedding: np.ndarray,
            poignancy_rating: int
    ):
        """
        Args:
            description (str): brief summary of the event
            poignancy_rating (int): how unimportant or important event was
        """
        self.id = id

        self.player_message = player_message
        self.character_response = character_response

        self.description = description
        self.embedding = embedding

        self.poignancy_rating = poignancy_rating
        self.timestamp = int(time.time())
