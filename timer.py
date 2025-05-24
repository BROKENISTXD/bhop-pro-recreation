import time

class Timer:
    """Simple timer for tracking level completion time."""

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        self.end_time = None

    def stop(self):
        if self.start_time is None:
            return 0
        self.end_time = time.time()
        return self.elapsed

    def reset(self):
        self.start_time = time.time()
        self.end_time = None

    @property
    def elapsed(self):
        if self.start_time is None:
            return 0
        end = self.end_time if self.end_time is not None else time.time()
        return end - self.start_time
