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
        #[MINIGAME-NAME, COMPLETED?] True=Completed, False=Not completed
        self.__minigames = [[IdBadge, False], [ReactionGame, False], [DownloadGame, False], [UploadGame, False], [RecordTemperatureGame, False]]
        self.__target_station = self.parent.wifi.requestStation(self.parent.badgeUID)

        if self.parent.isMinigameCompleted==True:#Was minigame completed?
        #if statement could be:
        #if self.parent.lastMinigame!=None:
        #then could remove the isMinigameCompleted variable.
            self.__minigames[self.__minigames.index([self.parent.lastMinigame, False])][1]=True #Change completed to True in minigames array
            self.parent.isMinigameCompleted=False #Set back to False
            self.parent.lastMinigame=None # set back to None

    def update(self):
        if self.state == RUNNING:
            uid, tag = self.parent.rfid.doRead(True)

            isAlive = self.parent.wifi.isAlive(self.parent.badgeUID)

            if isAlive:
                if tag == 'playerId':
                    if not self.parent.wifi.isAlive(uid):
                        self.parent.wifi.startVoting()
                        
                elif tag == ".votingHub":
                    self.parent.wifi.startVoting()

                elif tag == self.__target_station:
                    while True:#Loop until break(until an uncompleted minigame is chosen)
                        self.target_minigame = random.choice(self.__minigames)#Choose random minigame
                        if self.target_minigame[1]==False:#if minigame is not completed
                            break#stop loop
                    self.parent.currentMiniGame = self.target_minigame[0](self.parent)# Set currentMinigame to the mingame chosen
                else:
                    
                    self.parent.screen.drawText("GOTO: " + str(self.__target_station),0,0)
        else:
            if self.state == CREWMATE_WIN:
                while not any(self.parent.buttons.getPressedButtons()):
                    
                    self.parent.screen.drawText("Game Over! Crewmates Has won!")
            elif self.state == IMPOSTOR_WIN:
                while not any(self.parent.buttons.getPressedButtons()):
                    
                    self.parent.screen.drawText("Game Over! Impostors Has won!")
