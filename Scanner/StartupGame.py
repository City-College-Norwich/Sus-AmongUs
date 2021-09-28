from Minigame import Minigame
from IdleGame import IdleGame


class StartupGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == ".main":
            self.parent.wifi.sendRequest('StartGame')

    def alertFromServer(self, alert):
        if alert == 'GameStarted':
            self.parent.currentMiniGame = IdleGame()
