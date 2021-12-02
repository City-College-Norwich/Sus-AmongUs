from Minigames.Minigame import Minigame
from Minigames.GoodGuyGame import GoodGuyGame


class StartupGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent
        self.StartGameState = False

        print("Initiate StartupGame")
    
        # Tell player to scan badge
        self.parent.screen.clear()
        self.parent.screen.drawText('Scan Your ID', 0, 0)
        
    def update(self):
        uid, tag = self.parent.rfid.doRead(True)
        
        if tag == ".main":
            self.parent.wifi.startGame()

        elif self.parent.badgeUID is None and tag is not None:
            register = self.parent.wifi.registerUser(uid)
            if register:
                self.parent.badgeUID = uid
                self.StartGameState = True
            else:
                self.parent.screen.drawText('User already', 0, 0)
                self.parent.screen.drawText('registered', 0, 10)
                self.parent.screen.drawText('Use different ID', 0, 30)  

        if self.StartGameState == True:
            self.parent.screen.drawText("Scan start game tag", 0, 0)

