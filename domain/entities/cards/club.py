from domain.entities.cards.card import Card


class Club(Card):
    """
            This class represents the Card Club in the game.
    """

    def card_symbol(self):
        """
            :returns The Card Symbol.
        """
        return "\u2663"
