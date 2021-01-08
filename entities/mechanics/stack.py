from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade


class CardStack:

    def __init__(self):
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        self.stack = []
        for i in range(8):
            self.stack = self.stack + [possibleCards[x] for x in range(len(possibleCards))]

    def getStack(self):
        return self.stack
