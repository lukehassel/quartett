__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import random

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.player.player_base import PlayerBase
from ui.states.game_states import AskPlayerForCardAndPlayer


class Bot(PlayerBase):
    """
        This class represents a computer as a player.
        All methods are overridden from the PlayerBase class.
        For more information take a look at the PlayerBase class.
    """

    def __init__(self, name: str):
        """
            This constructor is overridden by the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().__init__(name)

    def add_quartet(self):
        super().add_quartet()

    def get_quartet_count(self):
        return super().get_quartet_count()

    def reset_quartet_count(self):
        super().reset_quartet_count()

    def get_random_player(self, players: [PlayerBase], current_player: PlayerBase):
        copy = players.copy()
        copy.remove(current_player)
        randIndexPlayer = random.randint(0, len(copy)-1)
        return copy[randIndexPlayer]

    def get_random_card(self):
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        randIndex = random.randint(0, 3)
        return possibleCards[randIndex]

    def ask_player_for_card(self, players: [PlayerBase], currentPlayer: PlayerBase):
        return AskPlayerForCardAndPlayer(self.get_random_player(players, currentPlayer), self.get_random_card())

    def get_name(self):
        return super().get_name()

    def get_hand(self):
        return super().get_hand()

    def add_card(self, card: Card):
        super().add_card(card)

    def set_hand(self, cards: [Card]):
        super().set_hand(cards)

    def has_card(self, card: Card):
        return super().has_card(card)

    def remove_card(self, card: Card):
        return super().remove_card(card)

    def reset_hand(self):
        super().reset_hand()

    def has_quartet(self):
        super().has_quartet()

    def remove_all_quartet(self, callback):
        super().remove_all_quartet(callback)

    def has_cards(self):
        return super().has_cards()
