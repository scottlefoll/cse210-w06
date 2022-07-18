"""Snake
Every great story seems to begin with a snake.

- Nicolas Cage -

Overview

Snake is a game in which the player seeks to eat food and earn points without 
running into their growing body.

Rules
Snake is played according to the following rules.

Players can move up, down, left and right by using the W, S, A and D keys.
Players try to eat the food by colliding with it.
Each food item is worth a random number of points between 1 and 5.
When a player eats the food...
The snake grows by one segment for each point the food is worth.
The food is reset to appear in a new location.
If a player collides with any segment of their own body the game is over.

Requirements

The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least 16 classes.
The program must remain true to game play described in the overview.

Have Some Fun

Have some fun by enhancing the game any way you like. A few ideas are as 
follows.

Enhanced food scoring and reset.
Enhanced game play and game over messages.
Enhanced game display, e.g. snake head or symbols"""

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
    cast.add_actor("snakes", Snake())
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