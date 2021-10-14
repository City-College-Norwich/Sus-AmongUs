from Minigames.GoodGuyGame import GoodGuyGame
from Minigames.Minigame import Minigame
from TimerHelper import *


class DownloadGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(parent)
        self.parent = parent
        self.progress = 0
        self.progress_width = 0
        self.timer = TimerHelper()
        self.timer.set(1000)
        self.rfid = False
        pass

    def update(self):
        self.rfid = self.parent.rfid.doRead()
        if self.rfid:
            if self.timer.check():
                self.progress_width = self.progress_width+self.progress
                self.progress = self.progress+10
                self.parent.screen.drawRectangle(10, 10, self.progress_width, 30)
                self.timer.set(1000)

                if self.progress > 100:
                    self.parent.wifi.sendRequest("minigameComplete?badgeUID=" + self.parent.badgeUID)
                    self.parent.currentMiniGame = GoodGuyGame()
        else:
            self.parent.screen.drawText("Error: Walked away from task", 0, 0)
