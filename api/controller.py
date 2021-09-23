
from flask import Flask
from model import model
app = Flask(__name__)

model = Model()

@app.route("/")
def home():
    return model.callHomepage()
    

@app.route("/minigameComplete")
def minigameComplete():
    args = request.args

    return model.minigameComplete(args["scannerId"])
