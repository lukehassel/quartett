__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"


class GameMechanics:

    def __init__(self):
        """
            Constructor which initializes the game.
        """


    def create_players(self):
        if gegner == 1:
            bot()
            pass
        else:
            player = int(input("Geben Sie Anzahl der Spieler an: "))
            if player <= 2 or player > 8:
                print("Versuchen Sie bitte nochmal")
                user_Interface()
            while counter < player:
                player_name = str(input("Wie heißen Sie: "))
                counter += 1
                name_list.append(player_name)
