exclusionList = ['boot.py', 'ssd1306.py', 'mfrc522.py', 'AutoDownloader.py']

import os
from Wifi import Wifi
import json
# get filelist (don't delete if we don't have new files to grab)

class DummyScreen:
    def drawText(msg, x, y):
        print ("{}, {}: {}".format(x, y, msg))
    
    def draw():
        pass

class DummyParent:
    screen = DummyScreen()


wifi = Wifi(DummyParent())

newFiles = wifi.sendRequest("AutoDownloader/GetFileList")
success = False

try:
    if newFiles == "":
        raise Exception('no files returned')
    newFiles = json.loads(newFiles)
    success = True
    print (newFiles)
except Exception as e:
    print ("failed to get files")
    print (e)


if success:
    path = os.getcwd()

    for cwd in os.walk(path):
        for fileName in os.listdir(cwd[0]):
            if fileName not in exclusionList:
                os.remove(os.path.join(cwd[0], fileName))
                print ("removing {}".format(fileName))

    print ("------------")
    for fileName in newFiles:
        print ("Creating: " + fileName)
        file = wifi.sendRequest("AutoDownloader/GetFile?fileName=" + fileName)
        if file != "":
            with open(file, 'w') as f:
                f.write(file)
        else:
            print("Error: Failed to get file: " + fileName + " - Aborting")
            break
    print ("")
    print ("Complete")
            
