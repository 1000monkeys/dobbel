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
    amount = input("How many dice? 3 4 or 5? Input q or Q to quit ")

    if amount[0].upper() == "Q":
        exit()

    amount = int(amount[0])
    if amount == 3 or amount == 4 or amount == 5:
        return amount
    else:
        print("Input three, four, five or Q to quit!")
        return handle_dice_input()


def handle_rolls(rolls):
    """
    does some post roll work on the results of the rolls
    shows totol value of rolls
    checks for triple sixes in rolls
    shows bottom of dice for rolls
    :param rolls: the rolls to process
    """

    # Build the string of the result
    print("################# Your result:")
    i = 0
    string = ""
    while i < len(rolls):
        string += "[" + str(rolls[i]) + "]"
        i += 1
    print(string)

    value = 0
    for roll in rolls:
        value += roll
    print("Total value of rolls is: " + str(value))

    six_count = 0
    for roll in rolls:
        if roll == 6:
            six_count += 1
    if six_count > 2:
        print("You rolled three sixes!!! YAY!")

    print("Bottom of the dice shows: ")
    string = ""
    bottom_value = 0
    for roll in rolls:
        temp = (7 - roll)
        bottom_value += temp
        string += "[" + str(temp) + "]"
    print(string)

    print("Total value of bottomside rolls is: " + str(bottom_value))


def rolling_dice(amount_of_dice):
    """
    Starts with a simple rolling animation using random non saved numbers
    while you get your result it saves the random rolls into a rolls list to be used later
    :param amount_of_dice: amount of rolls to put into the list
    :return: rolls in a list
    """

    print("################# Rolling!")
    # variable i only serves as a cap for amount of non result dice rolls
    i = 0
    rolls = []
    while len(rolls) < amount_of_dice:
        # loop as long as we do not have enough rolls in the result array compared to amount of dice
        roll = random.randint(1, 6)
        string = "[" + str(roll) + "]"

        if random.randint(0, 4) == 2 or i > 8:
            rolls.append(roll)
            string += " RESULT = " + string + " !!\n"
            # Result so send new line signal to continue rolling(maybe) on the next pass
            i = 0

        sys.stdout.write(string)

        time.sleep(0.25) # Sleep to simulate natural dice throwing
        i += 1

    return rolls


if __name__ == "__main__":
    print("Welcome to Kjell's crazy dice game!!")

    while True:
        amount = handle_dice_input()
        rolls = rolling_dice(amount)
        handle_rolls(rolls)
