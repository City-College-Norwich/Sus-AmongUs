from Minigames.Minigame import Minigame
from TimerHelper import TimerHelper


class Sabotage1(Minigame):

    def __init__(self, parent,sabotagedStation):
        super().__init__(parent)
        self.parent = parent
        self.__target_station = sabotagedStation
        self.alreadyScanned = False

    def update(self):
        if not self.alreadyScanned:
            self.parent.screen.drawText("GOTO: " + self.__target_station, 0, 0)
            if self.parent.rfid.doRead() == self.__target_station:
                self.parent.wifi.sendRequest("sabotageCompleted?badgeUID="+ self.parent.badgeUID)
                self.alreadyScanned = True
        else:
            self.parent.screen.drawText("Waiting for others to scan " + self.__target_station + "!", 0, 0)