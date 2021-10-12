import time


class TimerHelper:
    def __init__(self):
        self.start = time.time()*1000
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.start = time.time()*1000
        self.targetTime = timeInMS

    def check(self):
        delta = time.ticks_diff(time.time()*1000, self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False
