__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import random

from domain.entities.cards.card import Card
from domain.entities.cards.club import Club
from domain.entities.cards.diamond import Diamond
from domain.entities.cards.heart import Heart
from domain.entities.cards.spade import Spade
from domain.entities.player.player_base import PlayerBase
from ui.states.game_states import AskPlayerForCardAndPlayer


class Bot(PlayerBase):
    """
        This class represents a computer as a player.
        All methods are overridden from the PlayerBase class.
        For more information take a look at the PlayerBase class.
    """

    def __init__(self, name: str):
        """
            This constructor is overridden by the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().__init__(name)

    def reset(self):
        super().reset()

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

    def get_random_player(self, players: [PlayerBase], current_player: PlayerBase):
        """

               :param players:
               :param current_player:
               :return:
        """
        copy = players.copy()
        copy.remove(current_player)
        randIndexPlayer = random.randint(0, len(copy) - 1)
        return copy[randIndexPlayer]

    def get_random_card(self):
        """
            returns the random card.
        """
        randomType = random.randint(0, Card().possible_card_types().__len__() - 1)
        possibleCards = [Club(Card().possible_card_types()[randomType]),
                         Heart(Card().possible_card_types()[randomType]),
                         Spade(Card().possible_card_types()[randomType]),
                         Diamond(Card().possible_card_types()[randomType])]
        randIndex = random.randint(0, 3)
        return possibleCards[randIndex]

    def ask_player_for_card(self, players: [PlayerBase], currentPlayer: PlayerBase):
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
