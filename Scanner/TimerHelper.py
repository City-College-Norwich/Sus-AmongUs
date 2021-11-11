import time


class TimerHelper:
    def __init__(self):
        self.start = TimerHelper.__get_current_time()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.start = TimerHelper.__get_current_time()
        self.targetTime = timeInMS

    def check(self):
        delta = TimerHelper.__get_time_diff(TimerHelper.__get_current_time(), self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False

    @staticmethod
    def __get_current_time():
        tm = 0
        try:
            tm = time.ticks_ms()
        except AttributeError:
            tm = time.time()*1000

        return tm

    @staticmethod
    def __get_time_diff(tm1, tm2):
        diff = 0
        try:
            diff = time.ticks_diff(tm1, tm2)
        except AttributeError:
            diff = tm1 - tm2

        return diff
