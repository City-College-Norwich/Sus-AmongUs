exclusionList = ['/ssd1306.py', '/mfrc522.py', '/AD.py', '/Wifi.py']

import os
from Wifi import Wifi
import json
# get filelist (don't delete if we don't have new files to grab)

class DummyScreen:
    def drawText(self, msg, x, y):
        print ("{}, {}: {}".format(x, y, msg))
    
    def draw(self):
        pass
    
    def clear(self):
        pass
    
class DummyParent:
    screen = DummyScreen()

def walk(path):
    files = []
    if path == "/":
        path = ""
    for file in os.ilistdir(path):
        if file[1] == 16384:
            files += walk(path + "/" + file[0])
        else:
            files.append(path + "/" + file[0])
    return files

def dl():        
    wifi = Wifi(DummyParent())

    newFiles = wifi.getFileList()
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

        for fileName in walk(path):
            if fileName not in exclusionList:
                os.remove(fileName)
                print ("removing {}".format(fileName))
                    

        print ("------------")
        for fileName in newFiles:
            print ("Creating: " + fileName)
            file = wifi.getFile(fileName)
            if file != "":
                with open(fileName, 'w') as f:
                    f.write(file)
            else:
                print("Error: Failed to get file: " + fileName + " - Aborting")
                break
        print ("")
        print ("Complete")
                
