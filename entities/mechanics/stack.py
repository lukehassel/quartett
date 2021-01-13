import random

from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade
from entities.player.player_interface import PlayerInterface


class CardStack:

    def __init__(self):
        """
            a function to retrieve the cards in stack.
        """
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        self.stack = []
        for i in range(8):
            self.stack = self.stack + [possibleCards[x] for x in range(len(possibleCards))]

    def get_stack(self):
        """
            a function to retrieve the stack.
        """
        return self.stack

    def mix(self, players: [PlayerInterface]):
        """

        :param players:
        :return:
        """
        cardDict = {}
        for player in players:
            cardDict[player] = []

        if len(players) == 2:
            for i in range(10):

                for player in players:
                    cardDict[player] = cardDict[player] + [self.get_random_card()]

        else:
            playerIndex = 0
            while len(self.stack) > 0:
                cardDict[players[playerIndex]] = cardDict[players[playerIndex]] + [self.get_random_card()]
                if playerIndex > len(players)-2:
                    playerIndex = 0
                else:
                    playerIndex = playerIndex + 1

        for player in players:
            player.set_hand(cardDict[player])

    def is_stack_empty(self):
        """
            a function to check if the stack empty.
        """
        if self.stack.__len__() == 0:
            return True
        else:
            return False

    def get_random_card(self):
        """
            a function to give random card.
        """
        randIndex = random.randint(0, (self.stack.__len__() - 1))
        # print(str(randIndex) + "  " + str(self.stack.__len__()))
        randCard = self.stack[randIndex]
        del self.stack[randIndex]
        return randCard
