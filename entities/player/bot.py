__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import random

from entities.cards.card import Card
from entities.cards.club import Club
from entities.cards.diamond import Diamond
from entities.cards.heart import Heart
from entities.cards.spade import Spade
from entities.player.player_interface import PlayerInterface
from entities.states.game_states import AskPlayerForCardAndPlayer


class Bot(PlayerInterface):
    """
        This class represents a computer as a player.
        All methods are overridden from the PlayerInterface class.
        For more information take a look at the PlayerInterface class.
    """

    def __init__(self, name: str):
        """
            This constructor is overridden by the PlayerInterface class.
            For more information take a look at the PlayerInterface class.
        """
        super().__init__(name)

    def add_quartet(self):
        """

        :return:
        """
        super().add_quartet()

    def get_quartet_count(self):
        """
            returns the count from bot.
        """
        return super().get_quartet_count()

    def reset_quartet_count(self):
        """
            reset the count from bot.
        """
        super().reset_quartet_count()

    def get_random_player(self, players: [PlayerInterface], current_player: PlayerInterface):
        """

        :param players:
        :param current_player:
        :return:
        """
        copy = players.copy()
        copy.remove(current_player)
        randIndexPlayer = random.randint(0, len(copy)-1)
        return copy[randIndexPlayer]

    def get_random_card(self):
        """
            returns the random card.
        """
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        randIndex = random.randint(0, 3)
        return possibleCards[randIndex]

    def ask_player_for_card(self, players: [PlayerInterface], currentPlayer: PlayerInterface):
        """
            ask for the card.
        """
        return AskPlayerForCardAndPlayer(self.get_random_player(players, currentPlayer), self.get_random_card())

    def get_name(self):
        """
            give the name of the player.
        """
        return super().get_name()

    def get_hand(self):
        """
            what the player has in hand.
        """
        return super().get_hand()

    def add_card(self, card: Card):
        """
            add a card in the hand.
        """
        super().add_card(card)

    def set_hand(self, cards: [Card]):
        super().set_hand(cards)

    def has_card(self, card: Card):
        return super().has_card(card)

    def remove_card(self, card: Card):
        """
            remove the card.
        """
        return super().remove_card(card)

    def reset_hand(self):
        """
            reset the hand.
        """
        super().reset_hand()

    def has_quartet(self):
        """
           the player has a quartet.
        """
        super().has_quartet()

    def remove_all_quartet(self, callback):
        """
            remove all quartet.
        """
        super().remove_all_quartet(callback)

    def has_cards(self):
        """
            the player has the card.
        """
        return super().has_cards()
