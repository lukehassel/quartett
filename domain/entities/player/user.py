__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.cards.card import Card
from domain.entities.player.player_base import PlayerBase


class User(PlayerBase):
    """
        This class represents a real human as a player.
        All methods are overridden from the PlayerBase class.
        For more information take a look at the PlayerBase class.
    """

    def __init__(self, name: str):
        super().__init__(name)

    def get_name(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_name()

    def get_hand(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_hand()

    def reset(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().reset()

    def add_card(self, card: Card):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().add_card(card)

    def set_hand(self, cards: [Card]):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().set_hand(cards)

    def has_card(self, card: Card):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().has_card(card)

    def remove_card(self, card: Card):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().remove_card(card)

    def has_quartet(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().has_quartet()

    def remove_all_quartet(self, callback):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().remove_all_quartet(callback)

    def add_quartet(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().add_quartet()

    def get_quartet_count(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_quartet_count()

    def reset_quartet_count(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().reset_quartet_count()

    def has_cards(self):
        """
            All methods are overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().has_cards()

