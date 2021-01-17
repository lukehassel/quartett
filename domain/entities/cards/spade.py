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
