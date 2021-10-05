
from flask import Flask, request
from model import Model
app = Flask(__name__)

model = Model()

@app.route("/")
def home():
    return Model.callHomepage()

@app.route("/StartGame")
def startGame():
    return Model.startGame()

@app.route("/requestStation")
def requestStation():
    return Model.requestStation()

@app.route("/getTagName")
def getTagName():
    args = request.args
    return Model.getTagName(args["uid"])


@app.route("/minigameComplete")
def minigameComplete():
    args = request.args
    return Model.minigameComplete(args["scannerId"])
  

@app.route("/keepAlive")
def keepAlive():
    return Model.keepAlive()

if __name__ == '__main__': app.run(host='0.0.0.0')
