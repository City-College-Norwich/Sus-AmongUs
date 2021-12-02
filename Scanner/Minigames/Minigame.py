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
        """
        Initialize a Minigame object; sets parent object

        :param App parent:
        """
        self.parent = parent
    def update(self):
        """
        Cause an update to the Minigame objects state
        """
        pass


    def alertsFromServer(self, alerts):
        """
        Used to pass alerts to the Minigame object for processing, routing, or other interrupts that would otherwise
        be separate from the update loop

        :param dict alerts:
        """
        if 'GameRunning' in alerts and self.parent.state == self.parent.STARTING:
            self.parent.gotoIdleGame()
            self.parent.state = self.parent.RUNNING

        if 'Winner' in alerts and self.parent.state == self.parent.RUNNING:
            winner = alerts['Winner']
            if winner == "Crewmates":
                self.parent.gotoIdleGame()
                self.parent.state = self.parent.CREWMATE_WIN  # Crewmate win
            else:
                self.parent.gotoIdleGame()
                self.parent.state = self.parent.IMPOSTOR_WIN  # Impostor win


        if 'Sabotaged' in alerts and self.parent.state == self.parent.RUNNING:
            self.parent.state = self.parent.SABOTAGED
            sabotageType = alerts['Sabotaged']
            sabotageData = alerts['SabotageData']

            self.parent.gotoSabotageGame(sabotageType, sabotageData)


        elif 'Sabotaged' not in alerts and self.parent.state == self.parent.SABOTAGED:
            self.parent.state = self.parent.RUNNING
            self.parent.gotoIdleGame()

        if 'Start_Voting' in alerts and self.parent.state == self.parent.RUNNING:
            self.vType = alerts['Start_Voting']
            self.parent.gotoVotingGame(self.vType)


