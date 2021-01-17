__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import time

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.player.bot import Bot
from domain.entities.player.player_base import PlayerBase
from domain.entities.player.user import User
from domain.entities.stack import CardStack
from ui.states.game_states import AskPlayerForCardAndPlayer, PlayerDidCreatePlayerList, GameNewRoundState, GameExitState
from ui.ui_interface import UIInterface
import sys


class UIConsoleImpl(UIInterface):
    """
        This is the UI console Implementation. All methods are overridden from UIInterface.
    """

    def __init__(self):
        self.startNewGame = None

    def show_choose_players(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        players = []
        number = input("Bitte geben Sie die Anzahl der Spieler ein: ")
        if number == "exit":
            sys.exit("Spiel wurde beendet.")
        if number == "new":
            self.startNewGame()
            return None
        elif number.isdigit():
            if 1 < int(number) < 7:
                for i in range(1, int(number) + 1):
                    name = self.choose_name(i)
                    if name is None:
                        return None
                    player = self.bot_or_player(name)
                    if player is None:
                        return None
                    players.append(player)
                return PlayerDidCreatePlayerList(players)
            else:
                print("Anzahl der Spieler darf nur zwischen 2-8 sein.")
                return self.show_choose_players()

        else:
            self.show_unknown_input()
            return self.show_choose_players()

    def choose_name(self, player):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        name = input("Wie soll der " + str(player) + ". Spieler heißen: ")
        if name == "exit":
            sys.exit("Spiel wurde beendet.")
        if name == "new":
            self.startNewGame()
            return None
        return name

    def bot_or_player(self, name: str):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        value = input("Computerspieler = 0, Mensch = 1: ")

        if value == "exit":
            sys.exit("Spiel wurde beendet.")
        if value == "new":
            self.startNewGame()

        if value.isdigit():
            if int(value) == 0:
                return Bot(name)
            elif int(value):
                return User(name)
            else:
                self.show_unknown_input()
                return self.bot_or_player(name)
        else:
            self.show_unknown_input()
            return self.bot_or_player(name)

    def show_start_message(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("###################"), time.sleep(0.5)
        print("Spiel hat gestartet")
        print("Type new to restart the game.")
        print("Type exit to end the game.")
        print("###################"), time.sleep(0.5)

    def show_unknown_input(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Eingabe unbekannt.")

    def show_which_player(self, players: [PlayerBase], current_player: PlayerBase):
        """
            Asks over the ui which player and which card the user wants to choose.
            :param players: All possible players.
            :param current_player: The player which is the user himself.
        """
        print("Welchen spieler willst du nach einer Karte Fragen?")
        showPlayer = players.copy()
        showPlayer.remove(current_player)

        for i, val in enumerate(showPlayer):
            print("     [" + str(i) + "] Für Spieler " + val.get_name())
        player_option = input("Spieler: ")

        if player_option == "exit":
            return GameExitState()
        elif player_option == "new":
            self.startNewGame()

        card = self.show_which_card()

        if isinstance(card, type(GameExitState())):
            return card

        if player_option.isdigit():
            return AskPlayerForCardAndPlayer(showPlayer[int(player_option)], card)
        else:
            self.show_unknown_input()
            self.show_which_player(players, current_player)

    def show_new_round(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Neue Runde wird gestartet.")

    def show_which_card(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Nach welcher Karte willst du den Spieler Fragen?")
        possibleCards = [Club(), Diamond(), Heart(), Spade()]
        for i, card in enumerate(possibleCards):
            print("     [" + str(i) + "] Für " + card.card_symbol())
        card_option = input("Karte: ")
        if card_option.isdigit():
            return possibleCards[int(card_option)]
        elif card_option == "exit":
            return GameExitState()
        elif card_option == "new":
            self.startNewGame()
        else:
            self.show_unknown_input()
            return self.show_which_card()

    def show_current_move(self, player: PlayerBase):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Spieler " + player.get_name() + " ist dran.")

    def show_player_has_found_a_quartet(self, player: PlayerBase, card: Card):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Spieler " + player.get_name() + " hat ein Quartett mit dem Symbol " + card.card_symbol() + " gefunden.")

    def show_card_move(self, fromPlayer: PlayerBase, toPlayer: PlayerBase, card: Card):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print(
            "Spieler " + toPlayer.get_name() + " hat die Karte " + card.card_symbol() + " von " + fromPlayer.get_name() + " genommen.")

    def show_player_gets_card_from_stack(self, player: PlayerBase, card: Card):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Spieler " + player.get_name() + " hat die Karte " + card.card_symbol() + " vom Stapel gezogen")

    def show_current_hand(self, players: [PlayerBase], cardStack: CardStack):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
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
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("Es hat gewonnen:")
        for winner in winners:
            print("     " + winner.get_name())

    def set_callback_new_game(self, newGame):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        self.startNewGame = newGame
