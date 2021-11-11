
# =====================
# =====================
# copy/paste the code in this box here to any test
# it allows you to have the test in the /tests/ folder but import
# things above it.  The last line also loads up the MagicMock object
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from unittest.mock import MagicMock
# =====================
# =====================


# import actual used dependencies
import json
from Minigames.GoodGuyGame import GoodGuyGame
from Minigames.ImposterGame import ImposterGame

# create "mock" objects for all the imports we can't actually import
sys.modules['ssd1306'] = MagicMock()
sys.modules['machine'] = MagicMock()
sys.modules['mfrc522'] = MagicMock()
sys.modules['network'] = MagicMock()
sys.modules['urequests'] = MagicMock()
sys.modules['TimerHelper'] = MagicMock()
sys.modules['time'] = MagicMock()
sys.modules['StartupGame'] = MagicMock()


from App import App, KEEP_ALIVE_TIMEOUT

# --------------------------
class IsRunningSurrogate:
    def __init__(self, totalIterations=1):
        self.totalIterations = totalIterations
        self.currentIteration = 0

    def __bool__(self):
        if self.currentIteration < self.totalIterations:
            self.currentIteration+= 1
            return True
        return False
# --------------------------

def test_appCreated():
    app = App()

    assert isinstance(app, App)
#    assert app.id == 1
    assert app.isRunning == True

def test_app_runs():
    app = App()

    app.isRunning = IsRunningSurrogate(2)
    startupGame = MagicMock()
    startupGame.update = MagicMock()

    app.currentMiniGame = startupGame
    app.keepAlive = MagicMock()

    app.run()

    assert startupGame.update.call_count == 2
    assert app.keepAlive.call_count == 2

def test_app_keepAlive():
    app = App()

    app.wifi.sendRequest = MagicMock()
    app.wifi.sendRequest.return_value = json.dumps(list({"GameStarted","VotingStarted"}))

    app.keep_alive_timer.set = MagicMock()

    startupGame = MagicMock()
    startupGame.alertsFromServer = MagicMock()
    app.currentMiniGame = startupGame

    app.keepAlive()

    try:
        app.currentMiniGame.alertsFromServer.assert_called_with(set(["GameStarted", "VotingStarted"]))
        app.keep_alive_timer.set.assert_called_with(KEEP_ALIVE_TIMEOUT)
    except AssertionError as e:
        assert e == 0

def test_app_gotoIdleGame():
    app = App()

    app.gotoIdleGame()

    assert isinstance(app.currentMiniGame, GoodGuyGame) or isinstance(app.currentMiniGame, ImposterGame)

