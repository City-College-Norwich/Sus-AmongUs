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
        Minigame(self, parent)
        self.parent = parent
        # Add state variable 
        self.state = RUNNING
        
        # update bellow set with minigames
        self.__minigames = {IdBadge, ReactionGame}
        self.__target_station = self.parent.wifi.sendRequest("requestStation")

    def update(self): 
        # If state = running 
            # then do all of that
        if self.state == RUNNING
           
            targetRfidTag = self.parent.rfid.do_read()

            if targetRfidTag == self.__target_station:
                self.parent.currentMiniGame = random.choice(self.__minigames.__init__())
            else:
                self.parent.screen.clear_screen()
                self.parent.screen.display_text("GOTO: " + str(self.__target_station))
        #elseif gamestopped 
        #display game ended message 
        elif self.state == ENDED:
            self.parent.screen.display_text("Game Over!")

    def alertFromServer(self, alert):
        if alert == 'Gameended':
            self.state = ENDED
        # If alert = game ended
            #Then set state to game ended
        