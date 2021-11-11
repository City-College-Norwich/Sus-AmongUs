from Minigames.Minigame import Minigame
from TimerHelper import TimerHelper
import random


class ImposterGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.timer = TimerHelper()
        self.timer.set(60000)
    
    def update(self):
        if self.timer.check():
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=1")
            elif buttons[1] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=2")
            elif buttons[2] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=3")


        if self.parent.state ==self.parent.RUNNING:
           

            uid, tag = self.parent.rfid.doRead(True)
            if tag == 'playerId':
                if self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID) == "yes":
                    if uid != self.parent.badgeUID and self.parent.wifi.sendRequest("isAlive?badgeUID=" + uid) == 'yes':
                        self.parent.wifi.sendRequest("killPlayer?badgeUID="+uid)
                    else:
                        if self.parent.wifi.sendRequest("isAlive?badgeUID=" + uid) == "no":
                            self.parent.wifi.sendRequest("startVote")
                    
            if tag == ".votingHub":
                self.parent.wifi.sendRequest("startVote")
           

        elif self.parent.state == self.parent.CREWMATE_WIN:
            self.parent.screen.drawText("Game Over! Crewmates Has won!",0,0)
        elif self.parent.state == self.parent.IMPOSTOR_WIN:
            self.parent.screen.drawText("Game Over! Impostors Has won!",0,0)



    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if 'Sabotaged' in alerts:
            #Having the cooldown set here to 120 seconds will allow for the
            #60 seconds to complete the sabotage task (Crewmates) and also
            #the default 60 second cooldown for sabotages
            self.cooldown(120000)
