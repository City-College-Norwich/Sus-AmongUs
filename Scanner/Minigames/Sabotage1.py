from Minigame import Minigame
from TimerHelper import TimerHelper


class Sabotage1(Minigame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.__target_station = self.parent.wifi.send_request("requestStation")
        self.__sabotage_timer = TimerHelper()
        self.__sabotage_timer.set(60000)
        self.__participants = {}

    def update(self):
        self.parent.screen.clear_screen()
        self.parent.screen.display_text("GOTO: " + self.__target_station)
        if self.__sabotage_timer.check():
            self.parent.wifi.send_request("sabotageTimeout")

        if self.parent.rfid.do_read() == self.__target_station:
            self.__participants.add(self.parent.wifi.send_request("askForID"))

        if len(self.__participants) == 2:
            self.parent.wifi.send_request("sabotageCompleted")
