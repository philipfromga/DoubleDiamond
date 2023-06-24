#!/usr/bin/python3
import random

# Constants

SYMBOLS={"doubled":"<><>",
         "sevens":"7",
         "threebars":"≡",
         "twobars":"=",
         "onebar":"-",
         "cherry":"%"}
PAYOUTS={"doubled":1000,
         "sevens":80,
         "threebars":40,
         "twobars":25,
         "onebar":10,
         "anybar":5,
         "threecherry":10,
         "twocherry":5,
         "onecherry":2}

class Balance:
    total = 0

    def __init__(self,deposit):
        self.total = deposit
    def play_tokens(self,tokens):
        self.total -= tokens
    def add_winnings(self,tokens):
        self.total += tokens
        
def spinwheel():
    temp = list(SYMBOLS.values())
    randNum = random.randint(0,5)
    return temp[randNum]

def winner(tokens,bonus):
    print("The payline pays",tokens,"tokens")
    if(bonus>0):
        print("The bonus is ",bonus,"x the payline amount")
        total_tokens= tokens*bonus
        print("Total payout is",total_tokens,"tokens")
        return total_tokens
    else:
        print("Total payout is",tokens,"tokens")
        return tokens

#def test_payline(plTest = []):
#    print("There are ",plTest.count("<><>")," <><>")
#    print("There are ",plTest.count("7")," 7")
#    print("There are ",plTest.count("≡")," ≡")
#    print("There are ",plTest.count("=")," =")
#    print("There are ",plTest.count("-")," -")
#    print("There are ",plTest.count("%")," %")

def calc_payout(myPL = [],payout_balance = Balance(0)):
    print(*myPL,sep = "  ")
    bonus = 0
    # 3 Double Diamond
    if myPL.count("<><>") == 3:
        payout_balance.add_winnings(winner(PAYOUTS[doubled],bonus))
    # 2 Double Diamond defaults to 3 of a kind with a bonus
    elif myPL.count("<><>") == 2:
        bonus=4
        #find the payline amount with wildcards
        if myPL.count("7") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["sevens"],bonus))
        elif myPL.count("≡") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["threebars"],bonus))
        elif myPL.count("=") == 1:
           payout_balance.add_winnings(winner(PAYOUTS["twobars"],bonus))
        elif myPL.count("-") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["onebar"],bonus))
        elif myPL.count("%") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["threecherry"],bonus))
        else:
            print("An Error Occurred")
# 1 Double Diamond defaults to 3 of a kind or any bar but no pay out for mixed symbols
    elif myPL.count("<><>") == 1:
        bonus=2
        #find the payline amount with wildcards
        if myPL.count("7") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["sevens"],bonus))
        elif myPL.count("≡") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["threebars"],bonus))
        elif myPL.count("=") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["twobars"],bonus))
        elif myPL.count("-") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["onebar"],bonus))
        elif myPL.count("-")+myPL.count("=")+myPL.count("≡") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["anybar"],bonus))
        elif myPL.count("%") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["threecherry"],bonus))    
        elif myPL.count("%") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["twocherry"],bonus))    
        else:
            print("Nothing to win here")
    elif myPL.count("7") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["sevens"],bonus))
    elif myPL.count("≡") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["threebars"],bonus))
    elif myPL.count("=") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["twobars"],bonus))
    elif myPL.count("-") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["onebar"],bonus))
    elif myPL.count("-")+myPL.count("=")+myPL.count("≡") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["anybar"],bonus))
    elif myPL.count("%") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["threecherry"],bonus))
    elif myPL.count("%") == 2:
        payout_balance.add_winnings(winner(PAYOUTS["twocherry"],bonus))
    elif myPL.count("%") == 1:
        payout_balance.add_winnings(winner(PAYOUTS["onecherry"],bonus))
    else:
        print("Nothing to win here")

def main():
    myBalance = Balance(50)
    run_app="yes"
    while(run_app == "yes"):
        print("Your Slot Balance is ",myBalance.total)
        run_app = input("Would you like to play Double Diamond Slots? <Type yes or quit>  ")
        if run_app == "yes":
            run_app="yes"
            print("Playing 3 tokens")
            myBalance.play_tokens(3)
            payline = [spinwheel(),spinwheel(),spinwheel()]
            print(*payline,sep = "  ")
            print()
        #    test_payline(payline)
            print("Checking your winnings")
            calc_payout(payline,myBalance)
        elif run_app == "quit":
            run_app="no"
        else:
            run_app="yes"
            print("Please re-enter your choice")


#if __name__ == "__main__":
main()
