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
            A function to retrieve the name.
            :return:
                name of the user
        """
        return super().get_name()

    def get_hand(self):
        """
            A function to retrieve the points.
            :return:
        """
        return super().get_hand()

    def reset(self):
        super().reset()

    def add_card(self, card: Card):
        """

            :param card:
            :return:
        """
        super().add_card(card)

    def set_hand(self, cards: [Card]):
        """
            A function that adds a specific amount of points to the player.
            :param cards:
        """
        super().set_hand(cards)

    def has_card(self, card: Card):
        """
            a function for checking whether the player has the card or not.
            :param card:
            :return:
        """
        return super().has_card(card)

    def remove_card(self, card: Card):
        """
            remove the card
        """
        return super().remove_card(card)

    def reset_hand(self):
        """
            A function that resets the points to 0.
        """
        super().reset_hand()

    def has_quartet(self):
        """
            :return:
                user has quartet.
        """
        return super().has_quartet()

    def remove_all_quartet(self, callback):
        """
            A function which returns if the player has a quartet.
        """
        super().remove_all_quartet(callback)

    def add_quartet(self):
        """
            a function to add quartet in the count of player.
        :return:
        """
        super().add_quartet()

    def get_quartet_count(self):
        """
            a function to retrive the count of user.
            :return:
                count of the user.
        """
        return super().get_quartet_count()

    def reset_quartet_count(self):
        """
            A function that resets the points to 0.
            :return:
        """
        super().reset_quartet_count()

    def has_cards(self):
        return super().has_cards()

