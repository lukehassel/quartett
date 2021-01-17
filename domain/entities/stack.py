__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"


import random

from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.player.player_base import PlayerBase
from domain.entities.player.user import User


class CardStack:

    def __init__(self):
        """
            This constructor generates the card Stack.
        """
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        self.stack = []
        for i in range(8):
            self.stack = self.stack + [possibleCards[x] for x in range(len(possibleCards))]

    def get_stack(self):
        """
            A function to retrieve the stack.
            :returns The stack.
        """
        return self.stack

    def mix(self, players: [PlayerBase]):
        """
            This function is assigning random cards to the hands of the players.
            :param players: A list of all the players.

            Test Correct mixing with three players.
            >>> u1 = User("asdf")
            >>> u2 = User("asdf")
            >>> s.mix([u1,u2])
            >>> len(u1.get_hand())
            10
            >>> len(u2.get_hand())
            10

            Test if the length of the stack is 0 with three players.
            >>> u1 = User("asdf")
            >>> u2 = User("asdf")
            >>> u3 = User("asdf")
            >>> s.mix([u1,u2, u3])
            >>> s.get_stack().__len__()
            0

            Test if the length of the stack is 0 with eight players.
            >>> u1 = User("asdf")
            >>> u2 = User("asdf")
            >>> u3 = User("asdf")
            >>> u4 = User("asdf")
            >>> u5 = User("asdf")
            >>> u6 = User("asdf")
            >>> u7 = User("asdf")
            >>> u8 = User("asdf")
            >>> s.mix([u1, u2, u3, u4, u5, u6, u7, u8])
            >>> s.get_stack().__len__()
            0

            Test mixing for 9 players.
            >>> u1 = User("asdf")
            >>> u2 = User("asdf")
            >>> u3 = User("asdf")
            >>> u4 = User("asdf")
            >>> u5 = User("asdf")
            >>> u6 = User("asdf")
            >>> u7 = User("asdf")
            >>> u8 = User("asdf")
            >>> u9 = User("asdf")
            >>> s.mix([u1, u2, u3, u4, u5, u6, u7, u8, u9])
            Traceback (most recent call last):
            ...
            ValueError: Length can't be longer than 8.


            Test mixing for no players.
            >>> s.mix([])
            Traceback (most recent call last):
            ...
            ValueError: No Player defined.


                :param players:
                :return:
        """
        if len(players) == 0:
            raise ValueError("No Player defined.")
        else:
            if len(players)>8:
                raise ValueError("Length can't be longer than 8.")
            else:

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
                        if playerIndex > len(players) - 2:
                            playerIndex = 0
                        else:
                            playerIndex = playerIndex + 1

                for player in players:
                    player.set_hand(cardDict[player])

    def is_stack_empty(self):
        """
            A function to check if the stack empty.
            :returns True if the stack is empty. Else False.
        """
        if self.stack.__len__() == 0:
            return True
        else:
            return False

    def get_random_card(self):
        """
            :returns A random card from the stack.
        """
        randIndex = random.randint(0, (self.stack.__len__() - 1))
        # print(str(randIndex) + "  " + str(self.stack.__len__()))
        randCard = self.stack[randIndex]
        del self.stack[randIndex]
        return randCard


if __name__ == '__main__':
    import doctest

    doctest.testmod(extraglobs={'s': CardStack()})
