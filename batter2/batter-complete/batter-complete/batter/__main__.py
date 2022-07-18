"""Batter
Every great batter works on the theory
that the pitcher is more afraid of him
than he is of the pitcher.

- Ty Cobb -
Overview
Batter is a game where the player tries to destroy a wall of bricks by hitting a ball into them.

Rules
Batter is played according to the following rules.

The player can move left and right.
The player tries to bounce the ball into the wall of bricks.
The player earns points for each brick they break.
The player moves on to the next level when all the bricks are broken.
If the player misses the ball they lose a life.
The player has three lives during the game.

Requirements
The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least 16 classes.
The program must remain true to game play described in the overview.
Have Some Fun
Have some fun by enhancing the game any way you like. A few ideas are as follows.

Enhanced scoring and game reset.
Enhanced game play and game over messages.
Enhanced game display, e.g. brick animations"""


from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager


def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()