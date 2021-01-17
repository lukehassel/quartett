__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.cards.card import Card


class Spade(Card):

    """
            This class represents the Card Spade in the game.
    """

    def card_symbol(self):
        """
            :returns The Card Symbol.
        """
        return "\u2660"
