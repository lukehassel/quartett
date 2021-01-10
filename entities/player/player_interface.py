__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from entities.cards.card import Card
from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade


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

    def has_card(self, card: Card):
        for i in self.get_hand():
            if isinstance(i, type(card)):
                return True
        return False

    def remove_card(self, card: Card):
        for index, val in enumerate(self.get_hand()):
            if isinstance(val, type(card)):
                del self.get_hand()[index]
                return True
        return False

    def reset_hand(self):
        """
            A function that resets the points to 0.
        """
        self.hand = []

    def has_quartet(self):
        """
            A function which returns if the player has a quartett.
        """
        diamondCount = 0
        clubCount = 0
        heartCount = 0
        spadeCount = 0

        print("hand:" + str(self.get_hand()))

        for c in self.get_hand():
            if isinstance(c, type(Diamond())):
                diamondCount = diamondCount + 1
            elif isinstance(c, type(Spade())):
                spadeCount = spadeCount + 1
            elif isinstance(c, type(Heart())):
                heartCount = heartCount + 1
            elif isinstance(c, type(Club())):
                clubCount = clubCount + 1
        if diamondCount > 3:
            return True
        elif clubCount > 3:
            return True
        elif spadeCount > 3:
            return True
        elif heartCount > 3:
            return True
        else:
            return False

    def remove_all_quartet(self):
        """
            A function which returns if the player has a quartett.
        """
        possibleCards = [Club(), Diamond(), Heart(), Spade()]

        for c in possibleCards:

            count = sum(isinstance(i, type(c)) for i in self.hand)

            while count > 3:
                for q in range(4):
                    print(self.hand)

                    for i, o in enumerate(self.hand):
                        if isinstance(o, type(c)):
                            del self.hand[i]
                            print("ound")
                            break
                count = sum(isinstance(i, type(c)) for i in self.hand)
