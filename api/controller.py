
from flask import Flask, request
from model import Model
app = Flask(__name__)

model = Model()


@app.route("/")
def home():
    return model.callHomepage()


@app.route("/StartGame")
def startGame():
    return model.startGame()

@app.route("/requestStation")
def requestStation():
    return model.requestStation()


@app.route("/getTagName")
def getTagName():
    args = request.args
    return model.getTagName(args["uid"])


@app.route("/minigameComplete")
def minigameComplete():
    args = request.args
    return model.minigameComplete(args["badgeUID"])


@app.route("/keepAlive")
def keepAlive():
    return model.keepAlive()
  

@app.route("/deadBodyFound")
def deadBodyFound():
    args = request.args
    return model.deadbodyfound(args["badgeUID"])


@app.route("/registerUser")
def registerUser():
    args = request.args
    return model.registerUser(args["badgeUID"])

  
@app.route("/sabotage")
def sabotage():
    args = request.args
    return model.sabotage(args["sabotageType"])


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
