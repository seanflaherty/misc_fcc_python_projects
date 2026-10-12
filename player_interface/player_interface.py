"""Example module showing abstract classes/methods."""
import random
from abc import ABC, abstractmethod

class Player(ABC):
    """Game character class.

    Attributes:
        moves (list):
        position (tuple):
        path (list[tuple]):
    """
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        """Make move method."""
        # 1. Randomly select a move from the moves list
        move = random.choice(self.moves)

        # 2. Add coordinates to update the position attribute
        self.position = (self.position[0] + move[0], self.position[1] + move[1])

        # 3. Append the new position tuple to the path list
        self.path.append(self.position)

        # 4. Return the updated position
        return self.position

    @abstractmethod
    def level_up(self):
        """Abstract level up method."""

class Pawn(Player):
    """Class Player"""
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        self.moves.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
