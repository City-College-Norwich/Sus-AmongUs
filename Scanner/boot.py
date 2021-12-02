import os
import machine
machine.freq(240000000)

from Buttons import *

buttonManager = Buttons()
if buttonManager.getPressedButtons(0):
    from AD import *
    from Screen import *
    screen = Screen()
    screen.drawText("At Command", 0, 0)
    screen.drawText("prompt", 0, 10)
    screen.draw()

else:
    from App import App

    var = App()


