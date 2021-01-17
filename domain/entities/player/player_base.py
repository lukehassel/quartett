__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade


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

            >>> u1 = PlayerBase("")
            >>> u1.set_hand([Club(), Diamond(), Heart()])
            >>> u1.has_card(Diamond())
            True

            >>> u1.has_card(Club())
            True

            >>> u1.has_card( Heart())
            True

            >>> u1.remove_card( Heart())
            True

            >>> u1.remove_card( Diamond())
            True

            >>> u1.has_card(Heart())
            False

            >>> u1.has_card(Spade())
            False

            >>> u1.has_card(Diamond())
            False


        """
        for i in self.get_hand():
            if isinstance(i, type(card)) and i.get_card_type() == card.get_card_type():
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

    def reset(self):
        """
            A function that resets the points to 0.
        """
        self.hand = []
        self.quartetCount = 0

    def has_quartet(self):
        """
            A function which returns if the player has a quartet.



            >>> u1 = PlayerBase("")
            >>> u1.set_hand([Club(), Diamond(), Heart()])
            >>> u1.has_quartet()
            False

            >>> u1.set_hand([Club(), Diamond(), Heart(), Spade()])
            >>> u1.has_quartet()
            False

            >>> u1.set_hand([Club(), Diamond(), Diamond(), Diamond(), Diamond(), Diamond()])
            >>> u1.has_quartet()
            True

            >>> u1.set_hand([Club(), Spade(), Spade(), Spade(), Spade(), Diamond()])
            >>> u1.has_quartet()
            True

            >>> u1.set_hand([Heart(), Spade(), Spade(), Heart(), Heart(), Heart()])
            >>> u1.has_quartet()
            True


        """

        for c in self.get_hand():
            card_type = c.get_card_type()

            if any(x.get_card_type() == c.get_card_type() and isinstance(x, type(Diamond())) for x in
                   self.get_hand()) and any(
                x.get_card_type() == c.get_card_type() and isinstance(x, type(Spade())) for x in
                self.get_hand()) and any(
                x.get_card_type() == c.get_card_type() and isinstance(x, type(Heart())) for x in
                self.get_hand()) and any(
                x.get_card_type() == c.get_card_type() and isinstance(x, type(Club())) for x in self.get_hand()):
                return True

        return False

    def remove_all_quartet(self, callback):
        """
            A function which returns if the player has a quartett.
        """
        for ia, c in enumerate(self.get_hand()):
            card_type = c.get_card_type()

            for i, x in enumerate(self.get_hand()):
                if x.get_card_type() == c.get_card_type() and isinstance(x, type(Diamond())):
                    for i1, x1 in enumerate(self.get_hand()):
                        if x1.get_card_type() == c.get_card_type() and isinstance(x1, type(Spade())):
                            for i2, x2 in enumerate(self.get_hand()):
                                if x2.get_card_type() == c.get_card_type() and isinstance(x2, type(Heart())):
                                    for i3, x3 in enumerate(self.get_hand()):
                                        if x3.get_card_type() == c.get_card_type() and isinstance(x3, type(Club())):

                                            try:
                                                del self.hand[self.get_hand().index(x)]
                                                del self.hand[self.get_hand().index(x1)]
                                                del self.hand[self.get_hand().index(x2)]
                                                del self.hand[self.get_hand().index(x3)]
                                                callback(self, c)
                                                self.add_quartet()
                                            except:
                                                print("")


if __name__ == '__main__':
    import doctest

    doctest.testmod(extraglobs={'p': PlayerBase("")})
