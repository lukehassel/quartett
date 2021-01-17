from domain.entities.cards.card import Card


class Diamond(Card):

    def card_symbol(self):
        return "\u2666"

    def possible_card_types(self):
        return super().possible_card_types()

    def __init__(self, card_type=""):
        super().__init__(card_type)

    def get_card_type(self):
        return super().get_card_type()
