import time


class TimerHelper:
    def getMS(self):
        return time.time()*1000

    def __init__(self):
        self.start = self.getMS()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.start = self.getMS()
        self.targetTime = timeInMS

    def check(self):
        delta = (self.getMS() - self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False
