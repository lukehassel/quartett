__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import time

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.stack import CardStack
from domain.entities.player.player_base import PlayerBase
from ui.states.game_states import ChooseBotState, ChooseUserState, AskPlayerForCardAndPlayer
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
        """
            this function for the decision between bot and human.
        """
        opponent = int(input("Geben Sie [1] für Bot oder [2] für Mensch: "))
        if opponent == 1:
            return ChooseBotState()
        if opponent == 2:
            return ChooseUserState()
        else:
            self.show_unknown_input()
            self.show_option_bot_or_user()

    def show_unknown_input(self):
        """
            a function to wrong input.
        """
        print("Eingabe unbekannt.")


    def show_which_player(self, players: [PlayerBase], current_player: PlayerBase):
        """
            this function for asking about a player.
            :param players:
            :param current_player:
        """
        print("Welchen spieler willst du nach einer Karte Fragen?")
        showPlayer = players.copy()
        showPlayer.remove(current_player)

        for i, val in enumerate(showPlayer):
            print("     [" + str(i) + "] Für Spieler " + val.get_name())
        player_option = input("Spieler: ")

        card = self.show_which_card()

        if player_option.isdigit():
            return AskPlayerForCardAndPlayer(showPlayer[int(player_option)], card)
        else:
            self.show_unknown_input()
            self.show_which_player(players, current_player)

    def show_which_card(self):
        """
            this function for asking about a card.
            :return:
        """
        print("Nach welcher Karte willst du den Spieler Fragen?")
        possibleCards = [Club(), Diamond(), Heart(), Spade()]
        for i, card in enumerate(possibleCards):
            print("     [" + str(i) + "] Für " + card.card_symbol())
        card_option = input("Karte: ")
        if card_option.isdigit():
            return possibleCards[int(card_option)]
        else:
            self.show_unknown_input()
            return self.show_which_card()

    def show_current_move(self, player: PlayerBase):
        """
            this function shows that it is the next player's turn.
            :return:
                name of the player.
        """
        print("Spieler " + player.get_name() + " ist dran.")

    def show_player_has_found_a_quartet(self, player: PlayerBase, card: Card):
        """
            this function shows which player has a quartet.
            :return:
                name of the player
        """
        print("Spieler "+player.get_name()+" hat ein Quartett mit der Karte " + card.card_symbol() + " gefunden.")

    def show_card_move(self, fromPlayer: PlayerBase, toPlayer: PlayerBase, card: Card):
        """
            this function for moving the card from a player to another player.
            :param fromPlayer:
            :param toPlayer:
            :param card:
            :return:
                the names of the two players.
        """
        print(
            "Spieler " + toPlayer.get_name() + " hat die Karte " + card.card_symbol() + " von " + fromPlayer.get_name() + " genommen.")

    def show_player_gets_card_from_stack(self, player: PlayerBase, card: Card):
        """
            this function shows which player needs a card from the stack.
            :param player:
            :param card:
            :return:
                name of the player and the card symbol.
        """
        print("Spieler " + player.get_name() + " hat die Karte " + card.card_symbol() + " vom Stapel gezogen")

    def show_current_hand(self, players: [PlayerBase], cardStack: CardStack):
        """

            :param players:
            :param cardStack:
            :return:
        """
        print("----------------[Aktueller Spielstand]----------------")
        for player in players:
            hand = []
            for c in player.get_hand():
                hand.append(c.card_symbol())

            print(player.get_name() + " hat die Karten: " + str(hand))
        stack = []
        for c in cardStack.get_stack():
            stack.append(c.card_symbol())
        print("")
        print("Auf dem Stapel liegen die Karten: " + str(stack))
        print("")
        for player in players:
            print("Spieler " + player.get_name() + " hat " + str(player.get_quartet_count()) + " Quartette gefunden.")
        print("----------------[Aktueller Spielstand]----------------")

    def show_winner(self, winners: [PlayerBase]):
        print("Es hat gewonnen:")
        for winner in winners:
            print("     "+winner.get_name())