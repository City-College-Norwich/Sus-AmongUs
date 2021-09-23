import time

class TimerHelper:
    def __init__(self):
        pass

    def Set(self,timeInMS):
        self.start = time.ticks_ms()
        self.targetTime = timeInMS

    def Check(self):
        delta = time.ticks_diff(time.ticks_ms(), self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False
