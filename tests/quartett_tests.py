import unittest

from domain.entities.cards.card import Card
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
        test = CardStack()
        # print(test.get_stack())

        self.assertEqual(len(test.get_stack()), 32)

    def test_stack_mixing_with_two_players(self):
        test = CardStack()
        u1 = User("asdf")
        u2 = User("asdf")
        test.mix([u1, u2])
        print("stackLength: " + test.get_stack().__len__().__str__())

        hand = u1.get_hand()

        self.assertEqual(len(u1.get_hand()), 10)
        self.assertEqual(len(u2.get_hand()), 10)

    def test_stack_mixing_with_three_players(self):
        test = CardStack()
        u1 = User("asdf")
        u2 = User("asdf")
        u3 = User("asdf")
        test.mix([u1, u2, u3])
        print("stackLength: " + test.get_stack().__len__().__str__())

    def test_stack_mixing_with_eight_players(self):
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
        test = CardStack()
        print(test.get_random_card())
        print(test.get_stack().__len__())

        self.assertEqual(len(test.get_stack()), 31)

    def test_player_has_card(self):
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
        u1 = User("")

        u1.set_hand([Club(Card().possible_card_types()[2]), Diamond(Card().possible_card_types()[2]),
                     Spade(Card().possible_card_types()[2]), Heart(Card().possible_card_types()[2])])

        print(u1.has_quartet())
        self.assertEqual(u1.has_quartet(), True)

    def test_player_remove_quartet(self):
        u1 = User("")

        u1.set_hand([Club("B"), Diamond("B"), Spade("B"), Heart("B"), Diamond("B"), Diamond("B")])

        u1.remove_all_quartet(lambda: print("l"))
        print(str(u1.get_hand()))
        # self.assertEqual(len(u1.get_hand()), len([Club(), Diamond()]))


def test_console_ui(self):
    ui = UIConsoleImpl()

    print("you choose")
    print(ui.show_which_card())


def test_console_ui1(self):
    ui = UIConsoleImpl()

    u1 = User("asdf")
    u2 = User("asdfasd")
    print("you choose")
    print(ui.show_which_player([u1, u2]))


def test_has_no_cards(self):
    me = GameUseCase(UIConsoleImpl())

    u1 = User("asdf")
    u2 = User("asdfasd")
    u1.set_hand([Club(), Diamond(), Diamond(), Diamond(), Diamond(), Diamond()])
    u2.set_hand([Club()])
    self.assertEqual(me.players_have_cards([u1, u2]), True)
    u2.set_hand([])

    self.assertEqual(me.players_have_cards([u1, u2]), False)
