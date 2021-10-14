from Minigames.Minigame import Minigame
from TimerHelper import *


class UploadGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
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
                self.parent.screen.drawRectangle(10, 20, self.progress_width, 15)
                self.parent.screen.drawText(str(self.progress) + "%", 50, 45)
                self.timer.set(1000)


                if self.progress >= 100:
                    self.parent.wifi.sendRequest(self, "minigameComplete?badgeUID=" + self.parent.badgeUID)
                    self.parent.gotoGoodGuyGame()

            else:
                self.parent.screen.drawText("Error: Download Task not complete", 0, 0)
        else:
            self.parent.screen.drawText("Keep Scanning", 0, 0)
            self.parent.screen.drawRectangle(10, 20, self.progress_width, 15)
            self.parent.screen.drawText(str(self.progress) + "%", 50, 45)
