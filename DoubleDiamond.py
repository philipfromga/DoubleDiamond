#!/usr/bin/python3
import random
import time

# Constants

INIT_BALANCE=50
SYMBOLS=["<><>","7","≡","=","-","%"]
DD=1000
SEV=80
THREEB=40
TWOB=25
ONEB=10
ANYB=5
THREEC=10
TWOC=5
ONEC=2

print('This is Philip\'s Double Diamond Slots')

def spinwheel():
    randNum = random.randint(0,5)
    return SYMBOLS[randNum]
def test_payline(plTest = []):
    print("There are ",plTest.count("<><>")," <><>")
    print("There are ",plTest.count("7")," 7")
    print("There are ",plTest.count("≡")," ≡")
    print("There are ",plTest.count("=")," =")
    print("There are ",plTest.count("-")," -")
    print("There are ",plTest.count("%")," %")

def check_payout(myPL = []):
    print(*myPL,sep = "  ")
    bonus = 0
    # 3 Double Diamond
    if myPL.count("<><>") == 3:
        print("You win",DD,"tokens")
    # 2 Double Diamond defaults to 3 of a kind with a bonus
    elif myPL.count("<><>") == 2:
        bonus=4
        print("You win",bonus,"x the payline amount")
        #find the payline amount with wildcards
        if myPL.count("7") == 1:
            print("You win",SEV,"tokens")
            print("Total payout is",SEV*bonus,"tokens")
        elif myPL.count("≡") == 1:
            print("You win",THREEB,"tokens")
            print("Total payout is",THREEB*bonus,"tokens")
        elif myPL.count("=") == 1:
            print("You win",TWOB,"tokens")
            print("Total payout is",TWOB*bonus,"tokens")
        elif myPL.count("-") == 1:
            print("You win",ONEB,"tokens")
            print("Total payout is",ONEB*bonus,"tokens")
        elif myPL.count("%") == 1:
            print("You win",THREEC,"tokens")
            print("Total payout is",THREEC*bonus,"tokens")
        else:
            print("An Error Occurred")
    # 1 Double Diamond defaults to 3 of a kind or any bar but no pay out for mixed symbols
    elif myPL.count("<><>") == 1:
        bonus=2
        #find the payline amount with wildcards
        if myPL.count("7") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",SEV,"tokens")
            print("Total payout is",SEV*bonus,"tokens")
        elif myPL.count("≡") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",THREEB,"tokens")
            print("Total payout is",THREEB*bonus,"tokens")
        elif myPL.count("=") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",TWOB,"tokens")
            print("Total payout is",TWOB*bonus,"tokens")
        elif myPL.count("-") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",ONEB,"tokens")
            print("Total payout is",ONEB*bonus,"tokens")
        elif myPL.count("-")+myPL.count("=")+myPL.count("≡") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",ANYB,"tokens")
            print("Total payout is",ANYB*bonus,"tokens")
        elif myPL.count("%") == 2:
            print("You win",bonus,"x the payline amount")
            print("You win",THREEC,"tokens")    
            print("Total payout is",THREEC*bonus,"tokens")
        else:
            print("Nothing to win here")
    elif myPL.count("7") == 3:
        print("You win",SEV,"tokens")
    elif myPL.count("≡") == 3:
        print("You win",THREEB,"tokens")
    elif myPL.count("=") == 3:
        print("You win",TWOB,"tokens")
    elif myPL.count("-") == 3:
        print("You win",ONEB,"tokens")
    elif myPL.count("-")+myPL.count("=")+myPL.count("≡") == 3:
        print("You win",ANYB,"tokens")
    elif myPL.count("%") == 3:
        print("You win",THREEC,"tokens")
    elif myPL.count("%") == 2:
        print("You win",TWOC,"tokens")
    elif myPL.count("%") == 1:
        print("You win",ONEC,"tokens")
    else:
        print("Nothing to win here")

def main():
    payline = [spinwheel(),spinwheel(),spinwheel()]
    print(*payline,sep = "  ")
    print()
#    test_payline(payline)
    print("Checking your winnings")
    check_payout(payline)

#if __name__ == "__main__":
main()
