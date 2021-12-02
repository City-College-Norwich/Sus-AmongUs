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
        self.drawGUI()
        

    
    def update(self):
        if self.parent.state == self.parent.RUNNING:
            
            if self.timer.check():
                self.drawGUI()
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
                        self.scanCooldown.set(2000)
                    elif uid == self.parent.badgeUID:
                        self.parent.screen.drawText("are you ok?") #lol?
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
        self.parent.screen.drawText("Sabotage:", 0, 30)
        self.parent.screen.drawText("Buttons 1-3", 0, 40)
        self.parent.screen.drawText("o", 100, 10)
        self.parent.screen.drawText("o", 90, 18)
        self.parent.screen.drawText("o", 110, 18)
        if self.timer.check():
            self.parent.screen.drawText("Sabotage Ready", 0, 50)

