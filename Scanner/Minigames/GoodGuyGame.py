import random

from TimerHelper import TimerHelper
from Minigames.Minigame import Minigame

class GoodGuyGame(Minigame):

    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

        self.skipCooldown = TimerHelper()
        self.skipCooldown.set(1)

        self.__target_station = self.parent.wifi.requestStation(self.parent.badgeUID)

        if self.parent.isMinigameCompleted:
            self.parent.user_minigames_dict[self.parent.lastMinigame] = True
            self.parent.isMinigameCompleted = False
            self.parent.lastMinigame = None

    def update(self):
        if self.parent.state == self.parent.RUNNING:
            uid, tag = self.parent.rfid.doRead(True)


            isAlive = self.parent.wifi.isAlive(self.parent.badgeUID)

            if isAlive:
                if tag == 'playerId':
                    if not self.parent.wifi.isAlive(uid):
                        self.parent.wifi.startReportBody()

                elif tag == ".votingHub":
                    self.parent.wifi.startEmergency()

                elif tag == self.__target_station:
                    gameList = [game for game in self.parent.user_minigames_dict if not self.parent.user_minigames_dict[game]]
                    if not len(gameList):
                        for game in self.parent.user_minigames_dict:
                            self.parent.user_minigames_dict[game] = False
                            gameList = [game for game in self.parent.user_minigames_dict if not self.parent.user_minigames_dict[game]]
                    
                    self.parent.currentMiniGame = random.choice(gameList)(self.parent)
                    # sets current minigame to a random incomplete minigame

                else:
                    self.parent.screen.drawText("Crewmate", 0, 0)
                    self.parent.screen.drawText("GOTO: " + str(self.__target_station), 0, 10)
            else:#if player is dead
                self.parent.screen.clear()
                self.parent.screen.drawText("You are dead!", 0, 0)
        else:

            if self.parent.state == self.parent.CREWMATE_WIN:
                team = "Crewmates"
            elif self.parent.state == self.parent.IMPOSTOR_WIN:
                team = "Imposters"
            self.parent.screen.drawText("Game Over!", 0, 0)
            self.parent.screen.drawText("{} wins".format(team), 0, 20)

        if self.skipCooldown.check():
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[1] == 1 and self.skipCooldown.check():
                self.__target_station = self.parent.wifi.skipStation(self.__target_station)
                self.skipCooldown.set(60000)
