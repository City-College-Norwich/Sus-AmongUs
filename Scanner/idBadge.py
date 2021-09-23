from Minigame import Minigame

class ID_Badge(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self,parent)
        self.parent = parent

        self.parent.screen.display_text('Scan Card',0,0)

    def update(self):
        tag = self.parent.rfid.do_read()

        check_card(tag)

    def check_card(self, tag):
        if tag == 'card':#TODO- get format of id card data.
            self.parent.screen.clear_screen()
            self.parent.screen.display_text('Card Scanned',0,0)
            self.parent.wifi.send_request('minigameComplete?scannerId='+scannerId)

    def alertFromServer(self, alert):
        pass
