#!/usr/bin/python3
import random

print('This is Philip\'s Double Diamond Slots')

slots=["<><>","7","≡","=","-","%"]

def spin():
    randNum = random.randint(0,5)
    print( slots[randNum] )

spin()
