# timer_service.py

import time


class TimerError(Exception):
    """custom exception used to report errors in Timer class implemnentation"""
    pass


class TimerService:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            self.stop()

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def get_elapsed_time(self):
        """Return the elapsed time, in seconds"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        return time.perf_counter() - self._start_time

    def reset(self):
        """Reset the timer"""
        self.start()
