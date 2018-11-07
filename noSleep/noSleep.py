## Simple mouse jiggler used on windows 7

import time
import pyautogui
import sys

n = 0

def move():
    pyautogui.moveRel(1, 1)
    print('It Worked!' + str(n))
    time.sleep(180)

try:
    while True:
        n += 1
        move()
except KeyboardInterrupt:
    print('terminating program')
    sys.exit()
        
