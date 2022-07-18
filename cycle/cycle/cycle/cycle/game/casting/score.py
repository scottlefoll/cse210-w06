import constants
from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost.

    The responsibility of Score is to keep track of the points the player has
    earned by eating food, or by eating part of the other player's tail. It
    contains methods for adding and getting points. Client should use
    get_text() to get a string representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._snake1_points = 0
        self._snake2_points = 0
        self.add_points(0)

    def add_points(self, points, snake_number=0):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        if snake_number == 1:
            self._snake1_points += points

        elif snake_number == 2:
            self._snake2_points += points

        self.set_text(f"Score - Player 1: {self._snake1_points}, Player 2: {self._snake2_points} ")
