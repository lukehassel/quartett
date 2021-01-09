__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import time

from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade
from entities.player.player_interface import PlayerInterface
from entities.states.game_states import ChooseBotState, ChooseUserState, AskPlayerForACard
from ui.ui_interface import UIInterface


class UIConsoleImpl(UIInterface):
    """
        This is the UI console Implementation. All methods are overridden from UIInterface.
    """

    def show_start_message(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("###################"), time.sleep(0.5)
        print("Willkommen zum Spiel"), time.sleep(0.5)
        print("###################"), time.sleep(0.5)

        print("Es dürfen min 3 bis max 8 spieler zusammenspielen."), time.sleep(0.5)

    def show_option_bot_or_user(self):
        opponent = int(input("Geben Sie [1] für Bot oder [2] für Mensch: "))
        if opponent == 1:
            return ChooseBotState()
        if opponent == 2:
            return ChooseUserState()
        else:
            self.show_unknown_input()
            self.show_option_bot_or_user()

    def show_unknown_input(self):
        print("Eingabe unbekannt.")

    def show_which_player(self, players: [PlayerInterface]):
        print("Welchen spieler willst du nach einer Karte Fragen?")
        for i, player in enumerate(players):
            print("     [" + str(i) + "] Für Spieler " + player.get_name())
        player_option = input("Spieler: ")

        card = self.show_which_card()

        if player_option.isdigit():
            return AskPlayerForACard(players[int(player_option)])
        else:
            self.show_which_player(players)

    def show_which_card(self):
        print("Nach welcher Karte willst du den Spieler Fragen?")
        possibleCards = [Club(), Diamond(), Heart(), Spade()]
        for i, card in enumerate(possibleCards):
            print("     [" + str(i) + "] Für " + card.card_symbol())
        card_option = input("Karte: ")
        if card_option.isdigit():
            return possibleCards[int(card_option)]
        else:
            return self.show_which_card()
