from Minigame import Minigame

class Startupgame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self,parent)
        self.parent = parent

    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == ".main":
            self.parent.wifi.send_request('StartGame')
 

    def alertFromServer(self, alert):
        if alert == 'GameStarted':
            self.parent.currentMiniGame = IdleGame()
