import time


class TimerHelper:
    def __init__(self):
        self.start = time.ticks_ms()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.start = time.ticks_ms()
        self.targetTime = timeInMS

    def check(self):
        delta = time.ticks_diff(time.ticks_ms(), self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False
