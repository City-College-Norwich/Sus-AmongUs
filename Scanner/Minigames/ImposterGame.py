from Minigames.Minigame import Minigame
from TimerHelper import TimerHelper
import random


class ImposterGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.timer = TimerHelper()
        self.timer.set(60000)
        self.parent.screen.clear()
        self.parent.screen.drawText("Imposter", 0, 0)
    
    def update(self):
        if self.parent.state == self.parent.RUNNING:
            
            if self.timer.check():
                buttons = self.parent.buttons.getPressedButtons()
                if buttons[0] == 1:
                    self.parent.wifi.createSabotage("1")
                elif buttons[1] == 1:
                    self.parent.wifi.createSabotage("2")
                elif buttons[2] == 1:
                    self.parent.wifi.createSabotage("3")

            uid, tag = self.parent.rfid.doRead(True)
            isAlive = self.parent.wifi.isAlive(self.parent.badgeUID)
            if isAlive:
                if tag == 'playerId':
                    uidIsAlive = self.parent.wifi.isAlive(uid)
                    if uid != self.parent.badgeUID and uidIsAlive:
                        self.parent.wifi.killPlayer(self.parent.badgeUID, uid)
                    elif uid == self.parent.badgeUID:
                        self.parent.screen.drawText("are you ok?")
                    elif not uidIsAlive:
                        self.parent.wifi.startVoting()                     
                elif tag == ".votingHub":
                    self.parent.wifi.startVoting()
        elif self.parent.state == self.parent.CREWMATE_WIN:
            while not any(self.parent.buttons.getPressedButtons()):
                self.parent.screen.drawText("Game Over! Crewmates Has won!",0,0)
        elif self.parent.state == self.parent.IMPOSTOR_WIN:
            while not any(self.parent.buttons.getPressedButtons()):
                self.parent.screen.drawText("Game Over! Impostors Has won!",0,0)



    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if 'Sabotaged' in alerts:
            #Having the cooldown set here to 120 seconds will allow for the
            #60 seconds to complete the sabotage task (Crewmates) and also
            #the default 60 second cooldown for sabotages
            self.cooldown(120000)
