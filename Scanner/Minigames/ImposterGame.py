from Minigames.Minigame import Minigame
from TimeHelper import TimeHelper
import random

RUNNING = 0
CREWMATE_WIN = 1
IMPOSTOR_WIN = 2


class ImposterGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.timer = TimeHelper()
        self.cooldown = self.timer.set(60000)
    
    def update(self):
        if self.timer.check() == self.cooldown:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=1")
            elif buttons[1] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=2")
            elif buttons[2] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=3")


        if self.state == RUNNING:
           
            uid, tag = self.parent.rfid.doRead(True)
            if tag is not None and tag[:8] == 'playerId':
                if self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID) == "yes":   
                    # check if the first 7 characters == playerId
                    # if yes, then split at the colon and get the playerId number (just like in model)
                    # send that playerId in the sendRequest
                    #targetRfidTag = 'playerId:12'
                    if self.parent.wifi.sendRequest("isAlive?badgeUID=" + uid) == "no":
                        self.parent.wifi.sendRequest("startVote")
                    
           if tag == ".votingHub":
                self.parent.wifi.sendRequest("startVote")
                self.parent.gotoVotingGame()
            elif tag == self.__target_station:
                self.parent.currentMiniGame = random.choice(self.__minigames)(self.parent)
            elif:
                self.parent.screen.drawText("GOTO: " + str(self.__target_station),0,0)

        elif self.state == CREWMATE_WIN:
            self.parent.screen.display_text("Game Over! Crewmates Has won!")
        elif self.state == IMPOSTOR_WIN:
            self.parent.screen.display_text("Game Over! Impostors Has won!")


    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if 'Sabotaged' in alerts:
            #Having the cooldown set here to 120 seconds will allow for the
            #60 seconds to complete the sabotage task (Crewmates) and also
            #the default 60 second cooldown for sabotages
            self.cooldown(120000)
