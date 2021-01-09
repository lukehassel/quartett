__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import entities.mechanics.init_players as init_players
from ui.ui_interface import UIInterface


class GameMechanics:

    def __init__(self, ui: UIInterface):
        """
            Constructor which initializes the game.
        """
        self.players = init_players.createPlayers(self.ui)
        self.ui = ui

    def startGame(self):
        pass
    #     for player in self.players:
    #
    # def ask_player_for_card(self):
