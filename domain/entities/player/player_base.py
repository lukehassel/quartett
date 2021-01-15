__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
import doctest


class PlayerBase:
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
        self.quartetCount = 0

    def get_name(self):
        """
            A function to retrieve the name.
            :returns
                Name of the player.
        """
        return self.name

    def add_quartet(self):
        """
            a function to add quartet in the count of player.
        """
        self.quartetCount = self.quartetCount + 1

    def get_quartet_count(self):
        """
            :return: the count of player.
        """
        return self.quartetCount

    def reset_quartet_count(self):
        """
            the function to reset the count of player.
        """
        self.quartetCount = 0

    def has_cards(self):
        """
            a function to
            :return:
                card of the player
        """
        if len(self.hand) > 0:
            return True
        else:
            return False

    def get_hand(self):
        """
            A function to retrieve the points.
            :returns
                Points of the Player.
        """
        return self.hand

    def add_card(self, card: Card):
        """

            :param card:
            :return:
        """
        self.hand.append(card)

    def set_hand(self, cards: [Card]):
        """
            A function that adds a specific amount of points to the player.
            Args:
                 :param cards:
        """
        self.hand = cards

    def has_card(self, card: Card):
        """
            a function for checking whether the player has the card or not.
            :return:
                the player has a card or not.
        """
        for i in self.get_hand():
            if isinstance(i, type(card)):
                return True
        return False

    def remove_card(self, card: Card):
        """

            :param card:
            :return:
        """
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

if __name__ == '__main__':
    doctest.testmod()

    def doctest(self):
        """Return the factorial of n, an exact integer >= 0.

            >>> doctest()
            6
        """
        return 5

    def has_quartet(self):
        """
            A function which returns if the player has a quartet.
        """
        diamondCount = 0
        clubCount = 0
        heartCount = 0
        spadeCount = 0

        #print("hand:" + str(self.get_hand()))

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

    def remove_all_quartet(self, callback):
        """
            A function which returns if the player has a quartett.
        """
        possibleCards = [Club(), Diamond(), Heart(), Spade()]

        for c in possibleCards:

            count = sum(isinstance(i, type(c)) for i in self.hand)

            while count > 3:
                callback(self, c)
                self.add_quartet()
                for q in range(4):
                    # print(self.hand)

                    for i, o in enumerate(self.hand):
                        if isinstance(o, type(c)):
                            del self.hand[i]
                            break
                count = sum(isinstance(i, type(c)) for i in self.hand)
