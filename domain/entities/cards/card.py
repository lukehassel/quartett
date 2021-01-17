class Card(object):

    def __init__(self, card_type=""):
        self.card_type = card_type

    def possible_card_types(self):
        return ['A', 'K', 'D', 'B', '10', '9', '8', '7']

    def get_card_type(self):
        return self.card_type

    def card_symbol(self):
        pass
