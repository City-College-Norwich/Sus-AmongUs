import random

from Minigame import Minigame

'''
 game imports here                            
 from {file} import {class}                   
 e.g. from WiresMinigame import WiresMinigame 
'''
from IdBadge import IdBadge
from ReactionGame import ReactionGame

RUNNING = 0
ENDED = 1


class IdleGame(Minigame):

    def __init__(self, parent):
        super().__init__(parent)
        Minigame(self, parent)
        self.parent = parent
        # Add state variable 
        self.state = RUNNING
        
        # update bellow set with minigames
        self.__minigames = {IdBadge, ReactionGame}
        self.__target_station = self.parent.wifi.send_request("requestStation")

    def update(self):
        if self.state == RUNNING:
           
            targetRfidTag = self.parent.rfid.do_read()

            if targetRfidTag == self.__target_station:
                self.parent.currentMiniGame = random.choice(self.__minigames.__init__())
            else:
                self.parent.screen.clear_screen()
                self.parent.screen.display_text("GOTO: " + str(self.__target_station))
        elif self.state == ENDED:
            self.parent.screen.display_text("Game Over!")
