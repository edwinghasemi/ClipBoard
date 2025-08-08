import pyperclip as pc
import time
from datetime import datetime

## Globals  
clipBoard = []
logFile = "clipboardLog.txt"
lastPaste = ""



## Functions 
def printClipboard(limit = None):
    print("\n")
   
    ## Will print limit element if given, otherwise the whole clipboard
    limitToPrint = clipBoard[-limit:] if limit else clipBoard 

    for i, item in enumerate(limitToPrint, start=1):
        print(f"{i}: {item}")

def saveClipboard(clip):
    timeStamp = datetime.now().strftime("%Y-%m%-d% %H:%M:%S")
    with open(logFile, "a") as f:
        f.write(f"[{timeStamp}] {clip}\n")

def startUp():
    try:
        with open(logFile, "r") as f:
            clipBoard = [line.strip() for line in f.readlines()]
            print(clipBoard)
          
    except FileNotFoundError:
         clipBoard = []

def chooseFromHistory():
    number = 10
    printClipboard(number)

    try:
        indexInput = int(input("choose index"))
        if indexInput== 0:
                return 
        if 1 <= indexInput <= len(clipBoard[-number:]):
            newClip = clipBoard[-number:][indexInput - 1]
            pc.copy(newClip)
        else:
            return


    except ValueError:
        print("enter a number")

## Startup sequence
startUp()

## Main loop
try:
    while True:
        currentPaste = pc.paste()
        if currentPaste != lastPaste:
            clipBoard.append(f"[{datetime.now().strftime('%Y-%m%-%d %H:%M:%S')}] {currentPaste}")
            saveClipboard(currentPaste)
            printClipboard()
            lastPaste = currentPaste

        if input().lower == "pick":
            print(1)
            chooseFromHistory()

        time.sleep(1)


except KeyboardInterrupt:
    print("Exiting Clipboard program")

