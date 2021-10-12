from Minigames.Minigame import Minigame
from Minigames.GoodGuyGame import GoodGuyGame


class StartupGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

    
        # Save ID
        userID = self.parent.wifi.send_request('askForID')

        print("Initiate StartupGame")



        self.parent.id = userID
    
        # Tell player to scan badge
        self.parent.screen.display_text('Scan Card', 0, 0)
        
    def update(self):
        uid, tag = self.parent.rfid.do_read(returnUID = True)
        
        if tag == ".main":
            self.parent.wifi.send_request('StartGame')


        # ID badge scanned
        # If not recognised by server, tell server to register badge and ID
        
        elif tag is not None:
            self.parent.wifi.send_request('registerUser?scannerId='+self.parent.id+'&uid='+uid)

            print(tag)

