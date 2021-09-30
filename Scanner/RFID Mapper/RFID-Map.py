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
    