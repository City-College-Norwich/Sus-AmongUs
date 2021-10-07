from Minigame import Minigame
from IdleGame import IdleGame


class StartupGame(Minigame):
    def __init__(self, parent):
        super().__init__(self, parent)
        self.parent = parent

    
        # Save ID
        userID = self.parent.wifi.sendRequest('askForID')

        print("Initiate StartupGame")



        self.parent.id = userID
    
        # Tell player to scan badge
        self.parent.screen.drawText('Scan Card', 0, 0)
        
    def update(self):
        uid, tag = self.parent.rfid.doRead(returnUID = True)
        
        if tag == ".main":
            self.parent.wifi.sendRequest('StartGame')


        # ID badge scanned
        # If not recognised by server, tell server to register badge and ID
        
        elif tag not None:
            self.parent.wifi.sendRequest('registerUser?scannerId=' + self.parent.id + '&uid=' + uid)

            print(tag)

