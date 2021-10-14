from Minigames.Minigame import Minigame
from Minigames.GoodGuyGame import GoodGuyGame


class StartupGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent


        print("Initiate StartupGame")
    
        # Tell player to scan badge
        self.parent.screen.drawText('Scan Card', 0, 0)
        
    def update(self):
        uid, tag = self.parent.rfid.doRead(returnUID = True)
        
        if tag == ".main":
            self.parent.wifi.sendRequest('StartGame')

        elif self.parent.badgeUID is None and tag is not None:
            self.parent.badgeUID = uid
            self.parent.wifi.sendRequest('registerUser?badgeUID='+self.parent.badgeUID)


