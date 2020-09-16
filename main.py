import sys
import time
import random


def handle_dice_input():
    """
    Ask's for input on how many dice you want.
    If you input Q it will exit the program
    if your input is 3/4/5 it will return your input to the caller.
    if it is not 3/4/5 it displays a message on what you can input and restarts the function
    :return 3/4/5 as in how many dice.
    """
    amount = input("Input q or Q to quit, Disregards all other input.\nHow many dice? 3 4 or 5? >")
    if amount[0].upper() == "Q":  # Only really need the first character
        exit()
    elif int(amount[0]) == 3 or 4 or 5:
        return int(amount)
    else:
        print("Input three, four, five or Q to quit!")
        return handle_dice_input()


def handle_results(results):
    """
    does some post roll work on the results of the rolls
    shows your results together and on a new line the ttoal value of results
    checks for triple sixes in rolls
    shows bottom of dice for rolls and total value of bottom rolls
    :param rolls: the rolls to process
    """

    i, value, string = 0, 0, str()  # var i for count and value for total value from results
    while i < len(results):
        value += results[i]
        string += "[" + str(results[i]) + "]"
        i += 1
    print("################# Your result:\n" + string + "\nTotal value of rolls is: " + str(value))

    if results.count(6) > 2:
        print("You rolled three sixes!!! YAY!")

    string, bottom_value = "", 0
    for result in results:
        bottom_value += (7 - result)
        string += "[" + str(7 - result) + "]"
    print("Bottom of the dice shows:\n" + string + "\nTotal value of bottom side rolls is: " + str(bottom_value))


def rolling_dice(amount_of_dice):
    """
    Starts with a simple rolling animation using random non saved numbers
    while you get your result it saves the random rolls into a rolls list to be used later
    :param amount_of_dice: amount of rolls to put into the list
    :return: rolls in a list
    """

    print("################# Rolling!")
    # variable i only serves as a cap for amount of non result dice rolls
    i, results = 0, []
    while len(results) < amount_of_dice:  # loop as long as we do not have enough rolls in the result array
        roll = random.randint(1, 6)
        string = "[" + str(roll) + "]"

        if random.randint(0, 4) == 2 or i > 9:
            results.append(roll)
            string += " RESULT = " + string + " !!\n"
            i = 0

        sys.stdout.write(string)
        time.sleep(0.25)  # Sleep to simulate natural dice throwing
        i += 1

    return results


if __name__ == "__main__":
    print("Welcome to Kjell's crazy dice game!!")

    while True:
        handle_results(rolling_dice(handle_dice_input()))
