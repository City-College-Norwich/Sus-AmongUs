
from flask import Flask, request
from model import Model
app = Flask(__name__)

model = Model()


@app.route("/")
def home():
    return model.callHomepage()

@app.route
def setMaxMiniGames():
    return model.setMaxMiniGames(request.args["count"])

@app.route("/StartGame")
def startGame():
    return model.startGame()

@app.route("/requestStation")
def requestStation():
    return model.requestStation()


@app.route("/getTagName")
def getTagName():
    return model.getTagName(request.args["uid"])


@app.route("/minigameComplete")
def minigameComplete():
    return model.minigameComplete(request.args["scannerId"])


@app.route("/keepAlive")
def keepAlive():
    return model.keepAlive()
  

@app.route("/deadBodyFound")
def deadBodyFound():
    return model.deadbodyfound(request.args["playerId"])

  
@app.route("/askForID")
def askForID():
    return model.askForID()

  
@app.route("/registerUser")
def registerUser():
    args = request.args
    return model.registerUser(args["scannerId"], args["uid"])

  
@app.route("/sabotage")
def sabotage():
    return model.sabotage(request.args["sabotageType"])


@app.route("/getSabotageType")
def getSabotageType():
    return model.sabotage_type()


@app.route("/sabotageTimeout")
def sabotageTimeout():
    return model.sabotageTimeout()


@app.route("/sabotageCompleted")
def sabotageCompleted():
    return model.sabotageCompleted()


if __name__ == '__main__': app.run(host='0.0.0.0')
