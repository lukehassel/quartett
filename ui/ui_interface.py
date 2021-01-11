__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod

from entities.cards.card import Card
from entities.mechanics.stack import CardStack
from entities.player.player_interface import PlayerInterface


class UIInterface(ABC):
    @abstractmethod
    def show_start_message(self):
        """
            A method which shows the start Message and informations on how to quit and restart the game.
        """
        pass

    @abstractmethod
    def show_option_bot_or_user(self):
        pass

    @abstractmethod
    def show_unknown_input(self):
        pass

    @abstractmethod
    def show_player_has_found_a_quartet(self, player: PlayerInterface, card: Card):
        pass

    @abstractmethod
    def show_which_player(self, players: [PlayerInterface], current_player: PlayerInterface):
        pass

    @abstractmethod
    def show_which_card(self):
        pass

    @abstractmethod
    def show_current_hand(self, players: [PlayerInterface], stack: CardStack):
        pass

    @abstractmethod
    def show_current_move(self, player: PlayerInterface):
        pass

    @abstractmethod
    def show_player_gets_card_from_stack(self, player: PlayerInterface, card: Card):
        pass

    @abstractmethod
    def show_card_move(self, fromPlayer: PlayerInterface, toPlayer: PlayerInterface, card: Card):
        pass
