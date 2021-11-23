from Minigames.Minigame import Minigame
from TimerHelper import *


class DownloadGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self,parent)
        self.parent = parent
        self.progress = 0
        self.progress_width = 0
        self.timer = TimerHelper()
        self.timer.set(1000)
        self.rfid = False

        pass

    def update(self):
        self.rfid = self.parent.rfid.doRead()
        self.parent.screen.drawText("Download Game", 0, 0)
        if self.rfid:
            if self.timer.check():
                self.progress_width += random.choice(range(5, 16))
                self.progress = self.progress_width
                self.parent.screen.drawText("Keep Scanning", 0, 0)
                self.parent.screen.drawRectangle(10, 20, self.progress_width, 15)
                self.parent.screen.drawText(str(self.progress) + "%", 50, 45)
                self.timer.set(1000)

                if self.progress >= 100:
                    self.parent.wifi.completeMinigame(self.parent.badgeUID)
                    self.parent.isMinigameCompleted = True
                    self.parent.lastMinigame = DownloadGame
                    self.parent.gotoIdleGame()


        else:
            self.parent.screen.drawText("Keep Scanning", 0, 0)
            self.parent.screen.drawRectangle(10, 20, self.progress_width, 15)
            self.parent.screen.drawText(str(self.progress) + "%", 50, 45)
