__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from entities.cards.card import Card
from entities.player.player_interface import PlayerInterface


class User(PlayerInterface):
    """
        This class represents a real human as a player.
        All methods are overridden from the PlayerInterface class.
        For more information take a look at the PlayerInterface class.
    """

    def __init__(self, name: str):
        super().__init__(name)

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
        return super().has_quartet()

    def remove_all_quartet(self):
        super().remove_all_quartet()
