from domain.entities.cards.card import Card


class Diamond(Card):
    """
                This class represents the Card Diamond in the game.
    """

    def card_symbol(self):
        """
            :returns The Card Symbol.
        """
        return "\u2666"
