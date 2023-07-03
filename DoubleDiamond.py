#!/usr/bin/python3
import random
import art
import art.text_dic1

# Constants

art.text_dic1.block_dic["≡"] = ("\n .----------------. \n"
                                "| .--------------. |\n"
                                "| |    ______    | |\n"
                                "| |   |______|   | |\n"
                                "| |    ______    | |\n"
                                "| |   |______|   | |\n"
                                "| |    ______    | |\n"
                                "| |   |______|   | |\n"
                                "| |              | |\n"
                                "| '--------------' |\n"
                                " '----------------' \n")

art.text_dic1.block_dic["◇"] = ("\n .----------------. \n"
                                "| .--------------. |\n"
                                "| |  /\\      /\\  | |\n"
                                "| | //\\\\    //\\\\ | |\n"
                                "| |//  \\\\  //  \\\\| |\n"
                                "| |\\\\  //  \\\\  //| |\n"
                                "| | \\\\//    \\\\// | |\n"
                                "| |  \\/      \\/  | |\n"
                                "| |◇◇◇◇◇◇◇◇◇◇◇◇◇◇| |\n"
                                "| '--------------' |\n"
                                " '----------------' \n")

art.text_dic1.block_dic["%"] = ("\n .----------------. \n"
                                "| .--------------. |\n"
                                "| |         _    | |\n"
                                "| |    _   //    | |\n"
                                "| |   (_) //     | |\n"
                                "| |      // _    | |\n"
                                "| |    _   (_)   | |\n"
                                "| |   (_)        | |\n"
                                "| |              | |\n"
                                "| '--------------' |\n"
                                " '----------------' \n")

SYMBOLS = {"doubled": "◇",
           "sevens": "7",
           "threebars": "≡",
           "twobars": "=",
           "onebar": "-",
           "cherry": "%"}
PAYOUTS = {"doubled": 1000,
           "sevens": 80,
           "threebars": 40,
           "twobars": 25,
           "onebar": 10,
           "anybar": 5,
           "threecherry": 10,
           "twocherry": 5,
           "onecherry": 2}


class Balance:
    total = 0

    def __init__(self, deposit):
        self.total = deposit

    def play_tokens(self, tokens):
        self.total -= tokens

    def add_winnings(self, tokens):
        self.total += tokens


def spinwheel():
    temp = list(SYMBOLS.values())
    randnum = random.randint(0, 5)
    return temp[randnum]


def winner(tokens, bonus):
    print("The payline pays", tokens, "tokens")
    if bonus > 0:
        print("The bonus is ", bonus, "x the payline amount")
        total_tokens = tokens*bonus
        print("Total payout is", total_tokens, "tokens")
        return total_tokens
    else:
        print("Total payout is", tokens, "tokens")
        return tokens


def printpl(pllist):
    prtstring = ""
    for i in pllist:
        prtstring = prtstring + str(i)
    art.tprint(prtstring, font="block")


def calc_payout(mypl=[], payout_balance=Balance(0)):
    # print(*mypl,sep = "  ")
    printpl(mypl)
    bonus = 0
    # 3 Double Diamond
    if mypl.count("◇") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["doubled"], bonus))
    # 2 Double Diamond defaults to 3 of a kind with a bonus
    elif mypl.count("◇") == 2:
        bonus = 4
        # find the payline amount with wildcards
        if mypl.count("7") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["sevens"], bonus))
        elif mypl.count("≡") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["threebars"], bonus))
        elif mypl.count("=") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["twobars"], bonus))
        elif mypl.count("-") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["onebar"], bonus))
        elif mypl.count("%") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["threecherry"], bonus))
        else:
            print("An Error Occurred")
# 1 Double Diamond defaults to 3 of a kind or any
# bar but no pay out for mixed symbols
    elif mypl.count("◇") == 1:
        bonus = 2
        # find the payline amount with wildcards
        if mypl.count("7") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["sevens"], bonus))
        elif mypl.count("≡") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["threebars"], bonus))
        elif mypl.count("=") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["twobars"], bonus))
        elif mypl.count("-") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["onebar"], bonus))
        elif mypl.count("-")+mypl.count("=")+mypl.count("≡") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["anybar"], bonus))
        elif mypl.count("%") == 2:
            payout_balance.add_winnings(winner(PAYOUTS["threecherry"], bonus))
        elif mypl.count("%") == 1:
            payout_balance.add_winnings(winner(PAYOUTS["twocherry"], bonus))
        else:
            print("Nothing to win here")
    elif mypl.count("7") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["sevens"], bonus))
    elif mypl.count("≡") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["threebars"], bonus))
    elif mypl.count("=") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["twobars"], bonus))
    elif mypl.count("-") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["onebar"], bonus))
    elif mypl.count("-") + mypl.count("=")+mypl.count("≡") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["anybar"], bonus))
    elif mypl.count("%") == 3:
        payout_balance.add_winnings(winner(PAYOUTS["threecherry"], bonus))
    elif mypl.count("%") == 2:
        payout_balance.add_winnings(winner(PAYOUTS["twocherry"], bonus))
    elif mypl.count("%") == 1:
        payout_balance.add_winnings(winner(PAYOUTS["onecherry"], bonus))
    else:
        print("Nothing to win here")


def main():
    art.tprint("Double", font="1943")
    art.tprint(" Diamond", font="1943")
    art.tprint("  Slots", font="1943")
    art.tprint("◇7≡=-%", font="block")
    mybalance = Balance(50)
    run_app = "yes"
    while run_app == "yes":
        print("Your Slot Balance is ", mybalance.total)
        run_app = input("Would you like to play Double Diamond Slots?"
                        "<Type yes or quit>  ")
        if run_app == "yes":
            run_app = "yes"
            print("Playing 3 tokens")
            mybalance.play_tokens(3)
            payline = [spinwheel(), spinwheel(), spinwheel()]
            print()
        #    test_payline(payline)
            calc_payout(payline, mybalance)
            print("Checking your winnings")
        elif run_app == "quit":
            run_app = "no"
        else:
            run_app = "yes"
            print("Please re-enter your choice")


# if __name__ == "__main__":
main()
