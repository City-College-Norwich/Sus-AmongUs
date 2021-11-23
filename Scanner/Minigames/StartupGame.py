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
        self.parent.screen.drawText('Scan THE SUSSY Card', 0, 0)
        
    def update(self):
        uid, tag = self.parent.rfid.doRead(True)
        
        if tag == ".main":
            self.parent.wifi.startGame()

        elif self.parent.badgeUID is None and tag is not None:
            self.parent.badgeUID = uid
            self.parent.wifi.registerUser(self.parent.badgeUID)
            self.StartGameState = True

        if self.StartGameState == True:
            self.parent.screen.clear()
            self.parent.screen.drawText("sus",0,0)
            self.parent.screen.drawText("Scan start game tag", 10, 10)

