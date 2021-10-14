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
           
            targetRfidTag = self.parent.rfid.doRead()
            # check if the first 7 characters == playerId
            # if yes, then split at the colon and get the playerId number (just like in model)
            # send that playerId in the sendRequest

            #targetRfidTag = 'playerId:12'
            if targetRfidTag is not None and targetRfidTag[:8] == 'playerId':
                playerId = targetRfidTag.split(':')
                self.parent.wifi.sendRequest("deadBodyFound?badgeUID="+playerId[1])
            if targetRfidTag == self.__target_station:
                self.parent.currentMiniGame = random.choice(self.__minigames)(self.parent)
            else:
                self.parent.screen.drawText("GOTO: " + str(self.__target_station),0,0)
        else:
            if self.state == CREWMATE_WIN:
                self.parent.screen.drawText("Game Over! Crewmates Has won!")
            elif self.state == IMPOSTOR_WIN:
                self.parent.screen.drawText("Game Over! Impostors Has won!")
