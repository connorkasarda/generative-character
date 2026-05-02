import time


class Memory:
    """
    Encapsulates a recorded unit of the character's experiences
    """

    def __init__(self, description: str, poignancy_rating: int):
        """
        Args:
            description (str): brief summary of the event
            poignancy_rating (int): how unimportant or important event was
        """
        self.description = description
        self.poignancy_rating = poignancy_rating
        self.timestamp = int(time.time())
