"""
A utility script for mapping RFID UIDs to human readable names and storing the map as a csv file

The script reads a tags UID, checking if the tag is ok then requests a name from the user,
this will override any previously set names.

The script can be stopped by using an interrupt such as CTRL + C
"""

__docformat__ = 'restructuredtext'

import MFRC522_CrowPi
import csv
import os.path
import time

rdr = MFRC522.MFRC522()
FILE_PATH = "../../api/RFIDMap.csv"


# Create csv file if it doesnt exist
if not os.path.exists(FILE_PATH):
    open(FILE_PATH, "w").close()

while True:
    # Scan for cards
    (status,TagType) = rdr.MFRC522_Request(rdr.PICC_REQIDL)
    # If a card is found
    if status == rdr.MI_OK:
        print("Card found!")
        (status,uid) = rdr.MFRC522_Anticoll()
        if status == rdr.MI_OK:
            RFIDMap = {}
            uid = "0x%02x%02x%02x%02x" % (uid[0], uid[1], uid[2], uid[3])

            with open(FILE_PATH, mode='r') as csvfile:
                reader = csv.reader(csvfile)
                RFIDMap = {row[0]: row[1] for row in reader}

            file = open(FILE_PATH, "w+",newline="")
            name = input("What do you want to call this card? : ")
            CSVWriter = csv.writer(file,delimiter=',', quotechar='"')
            RFIDMap[uid] = name
            CSVWriter.writerows(RFIDMap.items())
            file.close()
    
    time.sleep(2)
    