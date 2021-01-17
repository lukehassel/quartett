__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import unittest

from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.player.user import User
from domain.entities.stack import CardStack
from domain.usecase.game_usecase import GameUseCase
from ui.ui_console_impl import UIConsoleImpl


class MyTestCase(unittest.TestCase):

    def test_stack_generation(self):
        """
        Test the generation of the stack.
        """
        test = CardStack()
        # print(test.get_stack())

        self.assertEqual(len(test.get_stack()), 32)

    def test_stack_mixing_with_two_players(self):
        """
                Mixing with two players
        """
        test = CardStack()
        u1 = User("asdf")
        u2 = User("asdf")
        test.mix([u1, u2])
        print("stackLength: " + test.get_stack().__len__().__str__())

        self.assertEqual(len(u1.get_hand()), 10)
        self.assertEqual(len(u2.get_hand()), 10)

    def test_stack_mixing_with_three_players(self):
        """
                Mixing with three players
        """
        test = CardStack()
        u1 = User("asdf")
        u2 = User("asdf")
        u3 = User("asdf")
        test.mix([u1, u2, u3])
        print("stackLength: " + test.get_stack().__len__().__str__())

    def test_stack_mixing_with_eight_players(self):
        """
                Mixing with eight players
        """
        test = CardStack()
        u1 = User("asdf")
        u2 = User("asdf")
        u3 = User("asdf")
        u4 = User("asdf")
        u5 = User("asdf")
        u6 = User("asdf")
        u7 = User("asdf")
        u8 = User("asdf")
        test.mix([u1, u2, u3, u4, u5, u6, u7, u8])
        print("stackLength: " + test.get_stack().__len__().__str__())

        self.assertEqual(len(u1.get_hand()), 4)
        self.assertEqual(len(u2.get_hand()), 4)
        self.assertEqual(len(u3.get_hand()), 4)
        self.assertEqual(len(u4.get_hand()), 4)
        self.assertEqual(len(u5.get_hand()), 4)
        self.assertEqual(len(u6.get_hand()), 4)
        self.assertEqual(len(u7.get_hand()), 4)
        self.assertEqual(len(u8.get_hand()), 4)

    def test_stack_random_card(self):
        """
                Selection of random card.
        """
        test = CardStack()
        print(test.get_random_card())
        print(test.get_stack().__len__())

    def test_player_has_card(self):
        """
                Test has_card function of player with a hand.
        """
        u1 = User("")
        u1.set_hand([Club(), Diamond()])

        self.assertEqual(u1.has_card(Diamond()), True)
        self.assertEqual(u1.has_card(Club()), True)
        self.assertEqual(u1.has_card(Heart()), False)
        self.assertEqual(u1.has_card(Spade()), False)

        u1.remove_card(Club())

        self.assertEqual(u1.has_card(Diamond()), True)
        self.assertEqual(u1.has_card(Club()), False)
        self.assertEqual(u1.has_card(Heart()), False)
        self.assertEqual(u1.has_card(Spade()), False)

        u1.remove_card(Diamond())

        self.assertEqual(u1.has_card(Diamond()), False)
        self.assertEqual(u1.has_card(Club()), False)
        self.assertEqual(u1.has_card(Heart()), False)
        self.assertEqual(u1.has_card(Spade()), False)

    def test_player_has_quartet(self):
        """
                Test if the player has a quartet.
        """
        u1 = User("")
        u1.set_hand([Club(), Diamond()])

        self.assertEqual(u1.has_quartet(), False)

        u1.set_hand([Club(), Diamond(), Diamond(), Diamond(), Diamond(), Diamond()])

        print(u1.has_quartet())
        self.assertEqual(u1.has_quartet(), True)

    def test_player_remove_quartet(self):
        """
                Test the removing of a quartet
        """

        u1 = User("")

        u1.set_hand([Club(), Diamond(), Diamond(), Diamond(), Diamond(), Diamond()])

        u1.remove_all_quartet()
        self.assertEqual(len(u1.get_hand()), len([Club(), Diamond()]))


    def test_console_ui(self):
        """
                Test ui.
        """
        ui = UIConsoleImpl()

        print("you choose")
        print(ui.show_which_card())

