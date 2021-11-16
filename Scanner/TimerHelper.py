"""
A timer helper specialised for accurate timers on either an micropython esp32 or python 3.5+ systems,
this module defines the following classes:

- TimerHelper, a timer helper.

"""

__docformat__ = 'restructuredtext'

import time


class TimerHelper:
    """
    This is a helper/util class for creating and managing timers

    TimerHelper objects can be made by calling TimerHelper() which then returns the helper object the timer can then
    be managed through this object such as setting start and target times and checking the progress of the timer

    target time are set by the set() method the timer can then be checked by the check()
    method
    """

    def __init__(self):
        """
        Initialize a TimerHelper object; initialize time objects.
        """
        self.start = TimerHelper.__get_current_time()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        """
        sets the start and target time of the timer

        :param int timeInMS: the target length of the timer in milliseconds
        """
        self.start = TimerHelper.__get_current_time()
        self.targetTime = timeInMS

    def check(self):
        """
        checks whether the timers target time has elapsed

        :rtype: bool
        :returns: Whether the timer's target time has elapsed
        """
        delta = TimerHelper.__get_time_diff(TimerHelper.__get_current_time(), self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False

    @staticmethod
    def __get_current_time():
        """
        Get the current unix epoch time in milliseconds

        :rtype: int
        :return: current time since unix epoch in milliseconds
        """
        tm = 0
        try:
            tm = time.ticks_ms()
        except AttributeError:
            tm = time.time()*1000

        return tm

    @staticmethod
    def __get_time_diff(tm1, tm2):
        """
        Used to get the absolute difference in milliseconds between two provided unix epoch times that are provided
        in milliseconds

        :param int tm1: first unix epoch time in milliseconds
        :param int tm2: second unix epoch time in milliseconds
        :rtype: int
        :return: absolute difference between two provided unix epoch times in milliseconds
        """
        diff = 0
        try:
            diff = time.ticks_diff(tm1, tm2)
        except AttributeError:
            diff = tm1 - tm2

        return abs(diff)
