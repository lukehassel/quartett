__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod

from domain.entities.cards.card import Card
from domain.entities.stack import CardStack
from domain.entities.player.player_base import PlayerBase


class UIInterface(ABC):
    @abstractmethod
    def show_start_message(self):
        """
            A method which shows the start Message and informations on how to quit and restart the game.
        """
        pass

    @abstractmethod
    def show_choose_players(self):
        pass

    @abstractmethod
    def choose_name(self, player):
        pass

    @abstractmethod
    def bot_or_player(self, name: str):
        pass

    @abstractmethod
    def show_unknown_input(self):
        pass

    @abstractmethod
    def show_player_has_found_a_quartet(self, player: PlayerBase, card: Card):
        pass

    @abstractmethod
    def show_which_player(self, players: [PlayerBase], current_player: PlayerBase):
        pass

    @abstractmethod
    def show_which_card(self):
        pass

    @abstractmethod
    def show_current_hand(self, players: [PlayerBase], stack: CardStack):
        pass

    @abstractmethod
    def show_current_move(self, player: PlayerBase):
        pass

    @abstractmethod
    def show_player_gets_card_from_stack(self, player: PlayerBase, card: Card):
        pass

    @abstractmethod
    def show_card_move(self, fromPlayer: PlayerBase, toPlayer: PlayerBase, card: Card):
        pass
    @abstractmethod
    def show_winner(self, winners: [PlayerBase]):
        pass

    @abstractmethod
    def show_new_round(self):
        pass

    @abstractmethod
    def set_callback_new_game(self, newGame):
        pass