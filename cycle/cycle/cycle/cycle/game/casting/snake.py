import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.services.timer_service import TimerService


class Snake(Actor):
    """
    A long limbless reptile.

    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, snake_number):
        super().__init__()
        self._segments = []
        self._snake_number = snake_number
        self._number_of_segments = constants.SNAKE_LENGTH
        self._prepare_body()
        self._t = TimerService()
        self._t.start()

    def get_segments(self):
        return self._segments

    def get_snake_number(self):
        return self._snake_number

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        if self._t.get_elapsed_time() > constants.SNAKE_GROWTH_INTERVAL:
            self.grow_tail(constants.SNAKE_GROWTH_RATE)
            self._t.reset()

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._snake_number == 1:
                segment.set_color(constants.SNAKE_COLOR1)
            else:
                segment.set_color(constants.SNAKE_COLOR2)
            self._segments.append(segment)

    def set_snake_number(self, snake_number):
        self._snake_number = snake_number

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            if self._snake_number == 1:
                position = Point(x - i * constants.CELL_SIZE, y - 50)
            else:
                position = Point(x - i * constants.CELL_SIZE, y - 100)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            if self._snake_number == 1:
                color = constants.YELLOW if i == 0 else constants.SNAKE_COLOR1
            else:
                color = constants.YELLOW if i == 0 else constants.SNAKE_COLOR2
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
