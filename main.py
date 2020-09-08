import time
import random


def handle_dice_input():
    """
    Ask's for input on how many dice you want.
    If you input Q it will exit the program
    if your input is 3/4/5 it will return your input to the caller.
    if it is not 3/4/5 it displays a message on what you can input and restarts the funcion
    :return 3/4/5 as in how many dice.
    """
    amount = input("How many dice? 3 4 or 5? Input q to quit ")

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


    bottom_value = 0
    string = ""
    print("Bottom of the dice shows: ")
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
    i = 0
    while i < 5:
        string = ""
        j = 0
        while j < amount_of_dice:
            string += "[" + str(random.randint(1, 6)) + "]"
            j += 1
        print(string)
        time.sleep(0.5)
        i += 1
    i = 0
    string = ""
    rolls = []
    while i < amount_of_dice:
        rolls.append(random.randint(1, 6))
        string += "[" + str(rolls[i]) + "]"
        i += 1
    print("################# Your result:")
    print(string)
    return rolls


if __name__ == "__main__":
    print("Welcome to Kjell's crazy dice game!!")

    while True:
        amount = handle_dice_input()
        rolls = rolling_dice(amount)
        handle_rolls(rolls)
