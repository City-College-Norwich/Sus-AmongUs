class Minigame:
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        pass


    def alertsFromServer(self, alerts):
        if 'GameRunning' in alerts and self.parent.state == self.parent.STARTING:
            self.parent.gotoIdleGame()
            self.parent.state = self.parent.RUNNING

        if 'Winner_Decided' in alerts:
            winner = alerts['Winner_Decided']
            if winner == "Crewmates":
                self.parent.gotoIdleGame()
                self.parent.currentMiniGame.state = 1  # Crewmate win
            else:
                self.parent.gotoIdleGame()
                self.parent.currentMiniGame.state = 2  # Impostor win


        if 'Sabotaged' in alerts:
            sabotage_type = alerts['Sabotaged']
            if sabotage_type == 1:
                sabotagedStation = alerts['SabotagedStation']
                self.parent.currentMiniGame = self.parent.gotoSabotageGame1(sabotagedStation)
            elif sabatage_type == 3:
                sabotagedStation = alerts['SabotagedStation']
                self.parent.currentMiniGame = self.parent.gotoSabotageGame3(sabotagedStation)

        if 'Start_Voting' in alerts and self.parent.state == self.parent.RUNNING:
            self.parent.gotoVotingGame()

            #TODO: REDO!
            # if sabotage_type == 1:
            #     self.parent.currentMiniGame = Sabotage1(parent)
            # elif sabotage_type == 2:
            #     self.parent.currentMiniGame = Sabotage2(parent)
            # else:
            #     self.parent.currentMiniGame = Sabotage3(parent)
