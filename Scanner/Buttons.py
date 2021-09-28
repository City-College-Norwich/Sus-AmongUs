from machine import Pin


class Buttons:

    def __init__(self):
        self.__button0 = Pin(34, Pin.IN, Pin.PULL_DOWN)
        self.__button1 = Pin(35, Pin.IN, Pin.PULL_DOWN)
        self.__button2 = Pin(36, Pin.IN, Pin.PULL_DOWN)
        self.__button3 = Pin(37, Pin.IN, Pin.PULL_DOWN)

    def getPressedButtons(self):
        return self.__button0.value(), self.__button1.value(), self.__button2.value(), self.__button3.value()
