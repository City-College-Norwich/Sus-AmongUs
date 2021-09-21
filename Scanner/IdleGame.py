
from Minigame import Minigame

'''
 game imports here                            
 from {file} import {class}                   
 e.g. from WiresMinigame import WiresMinigame 
'''
from StartupGame import StartupGame

class IdleGame(Minigame):

    def __init__(self, parent):
        Minigame(self, parent)
        self.parent = parent

    def update(self):
        tag = self.parent.rfid.do_read()
        minigame = None

        if tag == ".game/startupgame":
            self.parent.currentMiniGame = StartupGame()
            
        
    def alertFromServer(self, alert):
        pass
