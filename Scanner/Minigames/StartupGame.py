from Minigame import Minigame
from IdleGame import IdleGame


class StartupGame(Minigame):
    def __init__(self, parent):
        super().__init__(self, parent)
        self.parent = parent
        print("Initiate StartupGame")


    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == ".main":
            self.parent.wifi.send_request('StartGame')
