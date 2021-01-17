from domain.entities.cards.card import Card


class Heart(Card):

    """
            This class represents the Card Heart in the game.
    """

    def card_symbol(self):
        """
            :returns The Card Symbol.
        """
        return "\u2665"
