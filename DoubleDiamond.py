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

    def bal_print(self):
        print("")
        print("Your Slot Balance is ", self.total)
        print("")


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


def play_or_quit():
    ret_value = "yes"
    ret_value = input("Would you like to play Double Diamond Slots?"
                    "<Type yes or quit>  ")
    while ret_value not in ["yes","quit"]:
        ret_value = input("Please re-enter your choice < yes or quit >")
    return ret_value

def place_bet(avail_tokens):
    bet_amount = None
    while bet_amount is None:
        try:
            bet_amount = int(input("How many tokens do you want to bet?"))
        except ValueError:
            print("Invalid Entry")
        if avail_tokens-bet_amount <0:
            print("You don't have enough tokens")
            bet_amount = None
    return bet_amount


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
    art.tprint("Double", font="tarty3")
    art.tprint(" Diamond", font="tarty3")
    art.tprint("  Slots", font="tarty3")
    mybalance = Balance(50)
    run_app = "yes"
    while run_app == "yes":
        mybalance.bal_print()
        run_app = play_or_quit()
        if run_app == "yes":
            mybalance.play_tokens(place_bet(mybalance.total))
            payline = [spinwheel(), spinwheel(), spinwheel()]
            print()
            calc_payout(payline, mybalance)


if __name__ == '__main__':
    main()
