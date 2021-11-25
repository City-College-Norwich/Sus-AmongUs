"""
An abstract class intended to be used as a base for all minigames in the project,
this module defines te following classes:

- Minigame, a base for all minigames.

"""

__docformat__ = 'restructuredtext'


class Minigame:
  
    """
    This is a class intended to be an abstract base for all minigames

    Minigame objects should not be made directly but instead through a child/extension class which should override
    the update() and constructor methods

    The constructor should be overridden for each minigame for it's required initialisation and initial setup.

    The update method should also be overridden for each minigame for it's required updates on each game tick

    The alertsFromServer() method should not be overridden unless you know what you are doing

    """

    def __init__(self, parent):
        print ("--- minigame init")
        """
        Initialize a Minigame object; sets parent object

        :param App parent:
        """
        self.parent = parent
        self.sabotageOccured = False
    def update(self):
        print ("--- minigame update")
        """
        Cause an update to the Minigame objects state
        """
        pass


    def alertsFromServer(self, alerts):
        print ("--- minigame alertsFromServer")
        """
        Used to pass alerts to the Minigame object for processing, routing, or other interrupts that would otherwise
        be separate from the update loop

        :param dict alerts:
        """
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
            self.sabotageOccured = True
            sabotage_type = alerts['Sabotaged']
            if sabotage_type == 1 or sabotage_type == 3:
                sabotagedStation = alerts['SabotagedStation']
                self.parent.gotoSabotageStationGame(sabotage_type,sabotagedStation)
                
        elif self.sabotageOccured == True:
            self.sabotageOccured = False
            self.parent.gotoIdleGame()

        if 'Start_Voting' in alerts and self.parent.state == self.parent.RUNNING:
            self.vType = alerts['Start_Voting']
            self.parent.gotoVotingGame(self.vType)

            #TODO: REDO!
            # if sabotage_type == 1:
            #     self.parent.currentMiniGame = Sabotage1(parent)
            # elif sabotage_type == 2:
            #     self.parent.currentMiniGame = Sabotage2(parent)
            # else:
            #     self.parent.currentMiniGame = Sabotage3(parent)
