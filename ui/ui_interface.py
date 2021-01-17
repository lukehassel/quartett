__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod

from domain.entities.cards.card import Card
from domain.entities.player.player_base import PlayerBase
from domain.entities.stack import CardStack


class UIInterface(ABC):
    @abstractmethod
    def show_start_message(self):
        """
            A method which shows the start Message and informations on how to quit and restart the game.
        """
        pass

    @abstractmethod
    def show_choose_players(self):
        """
                Creates a player list with the ui.

                :return: The Game state PlayerDidCreatePlayerList with a list of the players.
        """
        pass

    @abstractmethod
    def choose_name(self, player):
        """
        Ask over the ui how a player should be named.

        :param player: The player count.
        :return: The name of the player
        """
        pass

    @abstractmethod
    def bot_or_player(self, name: str):
        """
                Ask over the ui if the player should be a bot or human player.
                :param name: Name of the player.
                :return: Returns either a Bot or a User object.
        """
        pass

    @abstractmethod
    def show_unknown_input(self):
        """
            A function to inform the user over the ui of an unknown input.
        """
        pass

    @abstractmethod
    def show_player_has_found_a_quartet(self, player: PlayerBase, card: Card):
        """
            This function shows which player has a quartet.
            :return:
                name of the player
        """
        pass

    @abstractmethod
    def show_which_player(self, players: [PlayerBase], current_player: PlayerBase):
        """
            Asks over the ui which player and which card the user wants to choose.
            :param players: All possible players.
            :param current_player: The player which is the user himself.
        """
        pass

    @abstractmethod
    def show_which_card(self):
        """
            Asks the user to choose a card.
            :return: The card the user choose.
        """
        pass

    @abstractmethod
    def show_current_hand(self, players: [PlayerBase], stack: CardStack):
        """
            show the current Game state with all the hands of all players.
            :param players: All players.
            :param cardStack: The Card Stack of the game.
        """
        pass

    @abstractmethod
    def show_current_move(self, player: PlayerBase):
        """
            This function shows that it is the next player's turn.
            :param player: The next player.
        """
        pass

    @abstractmethod
    def show_player_gets_card_from_stack(self, player: PlayerBase, card: Card):
        """
            This function shows which player takes a card from the stack.
            :param player: The Player which takes a card.
            :param card: The card.
        """
        pass

    @abstractmethod
    def show_card_move(self, fromPlayer: PlayerBase, toPlayer: PlayerBase, card: Card):
        """
            This function shows the moving of a card from a player to another player.
            :param fromPlayer: From player.
            :param toPlayer: To player.
            :param card: The Card.
        """
        pass

    @abstractmethod
    def show_winner(self, winners: [PlayerBase]):
        """
        Show who has won the game.
        :param winners: A list of all winners.
        """
        pass

    @abstractmethod
    def show_new_round(self):
        """
        Show that a new round has started.
        """
        pass

    @abstractmethod
    def set_callback_new_game(self, newGame):
        """
            Callback that gets called when a new game starts.
                :param newGame: The callback function.
                """
        pass
