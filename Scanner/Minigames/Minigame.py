class Minigame:
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        pass


    def alertsFromServer(self, alerts):
        if 'GameStarted' in alerts and self.parent.state == self.parent.STARTING:

            self.parent.gotoIdleGame()
            self.parent.state = self.parent.RUNNING

        if 'Crewmate_Win' in alerts:
            self.parent.gotoIdleGame()
            self.parent.currentMiniGame.state = 1  # Crewmate win

        elif "Impostor_Win" in alerts:
            self.parent.gotoIdleGame()
            self.parent.currentMiniGame.state = 2  # Impostor win

        if 'Sabotaged' in alerts:
            sabotage_type = self.parent.wifi.send_request("getSabotageType")
        
        if 'Voting' in alerts and self.parent.state == self.parent.RUNNING:
            self.parent.gotoVotingGame()


            #TODO: REDO!
            # if sabotage_type == 1:
            #     self.parent.currentMiniGame = Sabotage1(parent)
            # elif sabotage_type == 2:
            #     self.parent.currentMiniGame = Sabotage2(parent)
            # else:
            #     self.parent.currentMiniGame = Sabotage3(parent)
