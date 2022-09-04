from player import Player

class Utils():
    # displays a prompt and reads in the players name returning a string
    def get_player_name(self):
        # needs code here, see next function for idea of what
        player_name = input("Hello, What is your name? ")
        return player_name

    # ask the player to make a choice, takes a Player object
    # and returns a string
    def get_player_choice(self, player):
        print("%s, what do you choose?" % player.name)
        return input("> ")

    # determines who wins and updates score accordingly
    # takes in the player objects and their attack choices
    choices = ['R', 'P', 'S']

    def score_keep(self, you, your_choice, system, system_choice):
        if your_choice == "R" and system_choice == "P":
            system.score += 1
        elif system_choice == "R" and system_choice == "S":
            system.score += 1
        elif your_choice == "P" and system_choice == "S":
            system.score += 1
        elif your_choice == "P" and system_choice == "R":
            you.score += 1
        elif your_choice == "S" and system_choice == "P":
            you.score += 1
        elif system_choice == "S" and system_choice == "R":
            system.score += 1

    def winner(self, you, system):
        flag = "Not a Tie"
        if you.score > system.score:
            winner = you
            second_place = system
        elif you.score < system.score:
            winner = system
            second_place = you
        else:
            winner = you
            second_place = system
            flag = "Tie"
        return (winner, second_place, flag)

    def pretty_score_print(self, you, system):
        from texttable import Texttable
        t = Texttable()
        t.add_rows([['Name', 'Score'], [you.name, you.score], [system.name, system.score]])
        print(t.draw())



