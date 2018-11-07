## Adding a GUI at some point
## import tkinter as tk

import time
import os
import sys

os.system('clear')
n = x  = int(input("How long to work? *in seconds: "))
b = y = int(input("How long of a break? *in seconds: "))

def pom(n):
    while n > -1:
        mins, secs = divmod(n, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(str(timeformat), end='\r')
        time.sleep(1)
        n -= 1
    else:
        os.system('clear')
        print('Pom done, take a break.')
        rest(b)

def rest(b):
    while b > -1:
        mins, secs = divmod(b, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print(str(timeformat), end='\r')
        time.sleep(1)
        b -= 1
    else:
        b = y
        n = x
        os.system('clear')
        print('Back to making progress.')
        pom(n)
pom(n)
rest(b)
