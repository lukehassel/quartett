import random

from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade
from entities.player.player_interface import PlayerInterface


class CardStack:

    def __init__(self):
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        self.stack = []
        for i in range(8):
            self.stack = self.stack + [possibleCards[x] for x in range(len(possibleCards))]

    def getStack(self):
        return self.stack

    def mix(self, players: [PlayerInterface]):
        cardDict = {}
        for player in players:
            cardDict[player] = []

        if len(players) == 2:
            for i in range(10):

                for player in players:
                    cardDict[player] = cardDict[player] + [self.getRandomCard()]

        else:
            for i in self.stack:

                for player in players:
                    cardDict[player] = cardDict[player] + [self.getRandomCard()]

        for player in players:
            player.set_hand(cardDict[player])
            print(len(player.get_hand()))

    def isStackEmpty(self):
        if self.stack.__len__() == 0:
            return True
        else:
            return False

    def getRandomCard(self):
        randIndex = random.randint(0, (self.stack.__len__() - 1))
        # print(str(randIndex) + "  " + str(self.stack.__len__()))
        randCard = self.stack[randIndex]
        del self.stack[randIndex]
        return randCard
