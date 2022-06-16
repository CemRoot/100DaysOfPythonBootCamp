# guess-the-number-final
import random

EASY_LEVEL_TURNS = 10  # our lives are at the top of the screen
HARD_LEVEL_TURNS = 5
logo = """ 
  _______ _            _   _                 _                  _____                     _             
 |__   __| |          | \ | |               | |                / ____|                   (_)            
    | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _ 
    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` |
    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| |
    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |
                                                                                                   __/ |
                                                                                                  |___/ 
"""
print(logo)


def check_answer(guess, answer, turns):
    """
    This function checks if the user's guess is correct.
    :param guess:  The user's guess.
    :param answer:    The answer to the game.
    :param turns:   The number of turns the user has.
    :return:      True if the user wins, False if the user loses.
    """
    if guess > answer:
        print("You have " + str(turns) + " turns left. Your " + str(guess) + " is too high.")
        turns -= 1
    elif guess < answer:
        print("You have " + str(turns) + " turns left. Your " + str(guess) + " is too low.")
        turns -= 1

    else:
        print("You got it!")
        return True


def set_difficulty():
    """
    This function sets the difficulty of the game.
    :return:    The number of turns the user has.

    """
    level = input("Please choose a level: easy or hard: ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Please choose a valid level.")
        return set_difficulty()


def game():
    """
    This is the main game function.
    :return: None
    """
    print("Welcome to the number guessing game!")
    turns = set_difficulty()
    answer = random.randint(1, 100)
    while turns > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if check_answer(guess, answer, turns):
            return True  # if the user wins, return True
        turns -= 1
    print("You lost!")  # if the user loses, return False
    return False


game()  # start the game
