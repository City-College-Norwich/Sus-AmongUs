from Minigames.Minigame import Minigame
from TimerHelper import TimerHelper
import random


class ImposterGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.timer = TimerHelper()

        self.scanCooldown = TimerHelper()
        self.timer.set(60000)

        self.parent.screen.clear()
        self.sabotaging = False
        self.sabotageDrawn = False
        self.sabotageData = ""

        self.canMurder = False
        self.murderTimer = TimerHelper() 
        self.murderTimer.set(30000)

        self.murderDisplayed = False

        self.drawGUI()

    
    def update(self):
        if self.canMurder == False and self.murderTimer.check():
             self.parent.screen.drawText("Kill Ready", 0, 20)
             self.canMurder = True
             self.drawGUI()
       
        if self.murderDisplayed and self.scanCooldown.check():
            self.murderDisplayed = False
            self.drawGUI()

        if self.parent.state == self.parent.RUNNING or self.parent.state == self.parent.SABOTAGED:
            if self.sabotaging and not self.sabotageDrawn:
                self.sabotageDrawn = True
                self.drawGUI()

            if self.timer.check():
                self.drawGUI()
                buttons = self.parent.buttons.getPressedButtons()
                if buttons[0] == 1:
                    self.parent.wifi.createSabotage("1")
                    self.timer.set(120000)
                elif buttons[1] == 1:
                    self.parent.wifi.createSabotage("2")
                    self.timer.set(130000)
                elif buttons[2] == 1:
                    self.parent.wifi.createSabotage("3")
                    self.timer.set(150000)

            uid, tag = self.parent.rfid.doRead(True)
            isAlive = self.parent.wifi.isAlive(self.parent.badgeUID)
            if isAlive:
                if tag == 'playerId':
                    uidIsAlive = self.parent.wifi.isAlive(uid)
                    if uid != self.parent.badgeUID and uidIsAlive:
                        if self.canMurder == True:
                            self.parent.wifi.killPlayer(self.parent.badgeUID, uid)
                            self.parent.screen.clear()
                            self.parent.screen.drawText("MURDERZ!", 30, 10)
                            self.parent.screen.drawText("LoloLOLol", 26, 20)
                            self.murderDisplayed = True
                            self.scanCooldown.set(4000)
                            self.canMurder = False
                            self.murderTimer.set(30000)

                    elif uid == self.parent.badgeUID:
                        self.parent.screen.clear()
                        self.parent.screen.drawText("are you ok?") #lol?
                        self.murderDisplayed = True
                        self.scanCooldown.set(4000)

                    elif not uidIsAlive and self.scanCooldown.check():
                        self.parent.wifi.startReportBody()                     
                elif tag == ".votingHub":
                    self.parent.wifi.startEmergency()
            else:#if player is dead
                self.parent.screen.clear()
                self.parent.screen.drawText("You are dead!", 0, 0)

        elif self.parent.state == self.parent.CREWMATE_WIN:
            self.parent.screen.drawText("Game Over!",0,0)
            self.parent.screen.drawText(" Crewmates win!", 0, 20)
        elif self.parent.state == self.parent.IMPOSTOR_WIN:
            self.parent.screen.drawText("Game Over!",0,0)
            self.parent.screen.drawText("Impostors win!", 0, 20)


    def drawGUI(self):
        self.parent.screen.drawText("Imposter", 0, 0)
        if self.canMurder:
            self.parent.screen.drawText("Kill Ready", 0, 20)
        self.parent.screen.drawText("Sabotage:", 0, 30)
        self.parent.screen.drawText("Buttons 1-3", 0, 40)
        self.parent.screen.drawText("o", 100, 10)
        self.parent.screen.drawText("o", 90, 18)
        self.parent.screen.drawText("o", 110, 18)
        if self.timer.check():
            self.parent.screen.drawText("Sabotage Ready", 0, 50)

        if self.sabotageData:
            self.parent.screen.drawText(str(self.sabotageData), 0, 50)

    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)

        if 'Sabotaged' in alerts and not self.sabotaging:
            self.sabotaging = True
            self.sabotageDrawn = False
            self.sabotageData = alerts['SabotageData']
        if 'Sabotaged' not in alerts:
            self.sabotaging = False
