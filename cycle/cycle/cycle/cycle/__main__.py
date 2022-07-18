"""Cycle
The best rides are the ones where you
bite off much more than you can chew,
and live through it.

- Doug Bradbury -

Overview

Cycle is a game where the players try to cut each other off using cycles that
leave a trail behind them.

Rules

Cycle is played according to the following rules:`

Players can move up, down, left and right...
Player one moves using the W, S, A and D keys.
Player two moves using the I, K, J and L keys.
Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.
If a player collides with their opponent's trail...
A "game over" message is displayed in the middle of the screen.
The cycles turn white.
Players keep moving and turning but don't run into each other.

Requirements

The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least 16 classes.
The program must remain true to game play described in the overview.

Have Some Fun

Have some fun by enhancing the game any way you like. A few ideas are as
follows:

Enhanced scoring and game reset.
Enhanced game play and game over messages.
Enhanced game display, e.g. cycle and trails"""

import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake(1))
    snake = cast.get_first_actor("snakes")
    snake.turn_head(Point(-constants.CELL_SIZE, 0))
    cast.add_actor("snakes", Snake(2))
    cast.add_actor("scores", Score())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
