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
            a function to add a quartet quartet count of the player.
        """
        self.quartetCount = self.quartetCount + 1

    def get_quartet_count(self):
        """
            A function to retrieve the quartet count.
            :return: the quartet count.
        """
        return self.quartetCount

    def reset_quartet_count(self):
        """
            This function to resets the quartet count of the player.
        """
        self.quartetCount = 0

    def has_cards(self):
        """
            This function checks whether a player has a card on his hand.
            :return:
                True if the player has cards on this hand. False if not.
        """
        if len(self.hand) > 0:
            return True
        else:
            return False

    def get_hand(self):
        """
            :returns
                The current Hand of the player as a list.
        """
        return self.hand

    def add_card(self, card: Card):
        """
            Adds a card to the hand of the player.
            :param
                card: The card that should be added.
        """
        self.hand.append(card)

    def set_hand(self, cards: [Card]):
        """
            A function that sets the hand of the player.
            :param
                cards: Containing the cards that are going to be set to the players hand.
        """
        self.hand = cards

    def has_card(self, card: Card):
        """
            A function for checking whether the player has the card or not.
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
            if isinstance(i, type(card)):
                return True
        return False

    def remove_card(self, card: Card):
        """
            Removes a card from the players hand.
            :param
                card: The card that should be removed.
            :return: True if the removing was successful and False if not.
        """
        for index, val in enumerate(self.get_hand()):
            if isinstance(val, type(card)):
                del self.get_hand()[index]
                return True
        return False

    def reset(self):
        """
            A function that resets the quartet count to 0 and the hand to an empty list.
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
        diamondCount = 0
        clubCount = 0
        heartCount = 0
        spadeCount = 0

        # print("hand:" + str(self.get_hand()))

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
            Removes all quartet in a players hand.
            :param
                callback: Is called when a quartet is found.
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


if __name__ == '__main__':
    import doctest

    doctest.testmod(extraglobs={'p': PlayerBase("")})