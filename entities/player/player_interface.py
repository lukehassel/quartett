__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from entities.cards.card import Card


class PlayerInterface:
    """
        This Class represents a player in the game.
    """

    def __init__(self, name: str):
        """
            A Constructor which initializes a player with the corresponding name.
            The points are here set to 0.
            Args:
                 name: The name of a player.
        """
        self.hand = []
        self.name = name

    def get_name(self):
        """
            A function to retrieve the name.
            :returns
                Name of the player.
        """
        return self.name

    def get_hand(self):
        """
            A function to retrieve the points.
            :returns
                Points of the Player.
        """
        return self.hand

    def add_card(self, card: Card):
        self.hand.append(card)

    def set_hand(self, cards: [Card]):
        """
            A function that adds a specific amount of points to the player.
            Args:
                 :param cards:
        """
        self.hand = cards

    def has_card(self):
        pass

    def remove_card(self):
        pass

    def reset_hand(self):
        """
            A function that resets the points to 0.
        """
        self.hand = []

    def has_quartet(self):
        """
            A function which returns if the player has a quartett.
        """
        pass

    def remove_all_quartet(self):
        """
            A function which returns if the player has a quartett.
        """
        pass
