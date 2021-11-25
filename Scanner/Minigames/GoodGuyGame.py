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
       
        self.skipCooldown = TimeHelper()

        self.__target_station = self.parent.wifi.requestStation(self.parent.badgeUID)

        if self.parent.isMinigameCompleted:
            self.parent.user_minigames_dict[self.parent.lastMinigame] = True
            self.parent.isMinigameCompleted = False
            self.parent.lastMinigame = None

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

                    self.parent.currentMiniGame = random.choice([game for game in self.parent.user_minigames_dict if self.parent.user_minigames_dict[game]])
                    # sets current minigame to a random incomplete minigame

                else:

                    self.parent.screen.drawText("GOTO: " + str(self.__target_station), 0, 0)
        else:
            if self.state == CREWMATE_WIN:
                while not any(self.parent.buttons.getPressedButtons()):
                    self.parent.screen.drawText("Game Over! Crewmates Has won!")
            elif self.state == IMPOSTOR_WIN:
                while not any(self.parent.buttons.getPressedButtons()):
                    self.parent.screen.drawText("Game Over! Impostors Has won!")
                    
        if self.timer.check():
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                pass
            elif buttons[1] == 1 and self.skipCooldown.check():
                self.__target_station = self.parent.wifi.skipStation(self.__target_station,self.skipCooldown)
