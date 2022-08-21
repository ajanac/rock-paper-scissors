class Utils():
    # displays a prompt and reads in the players name returning a string
    def get_player_name(self):
        # needs code here, see next function for idea of what
        player_name = input("Hello, What is your name?")
        return player_name

    # ask the player to make a choice, takes a Player object
    # and returns a string
    def get_player_choice(self, player):
        print("%s, what do you choose?" % player.name)
        return input("> ")

    # determines who wins and updates score accordingly
    # takes in the player objects and their attack choices
    choices = ['R', 'P', 'S']

    def score_keep(self, player_one, player_one_choice, player_two, player_two_choice):
        if player_one_choice == player_two_choice:
            print("It is a tie.")
        elif player_one_choice == "R" and player_two_choice == "P":
            player_two.score += 1
        elif player_two_choice == "R" and player_two_choice == "S":
            player_two.score += 1
        elif player_one_choice == "P" and player_two_choice == "S":
            player_two.score += 1
        elif player_one_choice == "P" and player_two_choice == "R":
            player_one.score += 1
        elif player_one_choice == "S" and player_two_choice == "P":
            player_one.score += 1
        elif player_two_choice == "S" and player_two_choice == "R":
            player_two.score += 1

    def winner(self, player_one, player_two):
        winner_name = ""
        winner_score = -999
        if player_one.score > player_two.score:
            winner_name = player_one.name
            winner_score = player_one.score
        elif player_one.score < player_two.score:
            winner_name = player_two.name
            winner_score = player_two.score
        else:
            winner_name = "Tie"
        return (winner_name, winner_score)

