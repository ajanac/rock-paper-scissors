# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
# """
#  Rock Paper Scissors
# Rock Paper Scissors
#
# There are a number of functions that this program requires so let us have an overview of each.
#
# a random function: to generate rock, paper, or scissors.
# valid function: to check the validity of the move.
# result function: to declare the winner of the round.
# scorekeeper: to keep track of the score.
# The program requires the user to make the first move before it makes one the move.
# Once the move is validated the input is evaluated, the input entered could be a string or an alphabet.
# After evaluating the input string a winner is decided by the result function and the score of the round is updated by the scorekeeper function.
#
# """

""" Rock Paper Scissors
----------------------------------------
"""
from player import Player
from utils import Utils

import logging
import random
import re

logger = logging.getLogger(__name__)

def valid_user_choice(user_choice):
    if not re.match("[SsRrPp]", user_choice):
        return True
    else:
        return False

def start_game():
    print("Rock, Paper, Scissors - Game!!!")
    util_obj = Utils()
    choices = ['R', 'P', 'S']
    your_name = util_obj.get_player_name()
    you = Player(your_name, 0)
    system = Player("System", 0)
    while True:
        print("*****************************")
        your_choice = input("Choose your weapon [R]ock | [P]aper | [S]cissors: ").upper()
        if valid_user_choice(your_choice):
            print("You choose an invalid input")
            print("Please choose a valid letter: ")
            continue
        print(f"{you.name}'s choice: {your_choice}")
        system_choice = random.choice(choices)
        print(f"{system.name}'s choice: {system_choice}")
        util_obj.score_keep(you, your_choice, system, system_choice)
        util_obj.pretty_score_print(you, system)
        wanna_play_again = input("Do you want to continue [Y]es | [N]o? ")
        if wanna_play_again.upper() == 'Y':
            continue
        else:
            (winner, second_place, flag) = util_obj.winner(you, system)
            if flag == "Not a Tie":
                print(f"winner is {winner.name}")
                util_obj.pretty_score_print(winner, second_place)
            else:
                util_obj.pretty_score_print(winner, second_place)
                print("It is a tie")
            break

if __name__ == '__main__':
    start_game()
    #need to come back for fixing the output
    #add exception as well as unit testing
    #need to fix the "Textable library : downloaded in the local pycharm project but not here.
