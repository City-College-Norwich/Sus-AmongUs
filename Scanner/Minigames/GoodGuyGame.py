import random

from Minigames.Minigame import Minigame
from Minigames.IdBadge import IdBadge
from Minigames.ReactionGame import ReactionGame
from Minigames.DownloadGame import DownloadGame
from Minigames.UploadGame import UploadGame
from Minigames.RecordTemperatureGame import RecordTemperatureGame


RUNNING = 0
CREWMATE_WIN = 1
IMPOSTOR_WIN = 2

class GoodGuyGame(Minigame):

    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent
        # Add state variable 
        self.state = RUNNING
        
        # update bellow set with minigames
        self.__minigames = [IdBadge, ReactionGame, DownloadGame, UploadGame, RecordTemperatureGame]
        self.__target_station = self.parent.wifi.sendRequest("requestStation")

    def update(self):
        if self.state == RUNNING:
            uid, tag = self.parent.rfid.doRead(True)

            # Check if the user scanned is dead, and if so, start the voting process
            if tag is not None and tag[:8] == 'playerId':
                if self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID) == "yes":  
                    if self.parent.wifi.sendRequest("isAlive?badgeUID=" + uid) == "no":
                        self.parent.wifi.sendRequest("startVote")

            if tag == ".votingHub":
                self.parent.wifi.sendRequest("startVote")
                self.parent.gotoVotingGame()
                
            elif tag == self.__target_station:
                self.parent.currentMiniGame = random.choice(self.__minigames)(self.parent)
            elif:
                self.parent.screen.drawText("GOTO: " + str(self.__target_station),0,0)
        else:
            if self.state == CREWMATE_WIN:
                self.parent.screen.drawText("Game Over! Crewmates Has won!")
            elif self.state == IMPOSTOR_WIN:
                self.parent.screen.drawText("Game Over! Impostors Has won!")
