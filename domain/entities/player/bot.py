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
        Some methods are overridden from the PlayerBase class.
        For more information take a look at the PlayerBase class.
    """

    def __init__(self, name: str):
        """
            This constructor is overridden by the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().__init__(name)

    def reset(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().reset()

    def add_quartet(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().add_quartet()

    def get_quartet_count(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_quartet_count()

    def reset_quartet_count(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().reset_quartet_count()

    def get_random_player(self, players: [PlayerBase], current_player: PlayerBase):
        """
            :returns A random player from all possible players except the bot himself.
            :param
                players: All possible players in the game.
                current_player: The player himself.
        """
        copy = players.copy()
        copy.remove(current_player)
        randIndexPlayer = random.randint(0, len(copy) - 1)
        return copy[randIndexPlayer]

    def get_random_card(self):
        """
            :returns A random card from all possible cards.
        """
        possibleCards = [Club(), Heart(), Spade(), Diamond()]
        randIndex = random.randint(0, 3)
        return possibleCards[randIndex]

    def ask_player_for_card(self, players: [PlayerBase], currentPlayer: PlayerBase):
        """
            :returns The AskPlayerForCardAndPlayer Game state which contains a random player and a random card.
            :param
                players: A list of all possible players.
                currentPlayer: The current player which executes the action.
        """
        return AskPlayerForCardAndPlayer(self.get_random_player(players, currentPlayer), self.get_random_card())

    def get_name(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_name()

    def get_hand(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().get_hand()

    def add_card(self, card: Card):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().add_card(card)

    def set_hand(self, cards: [Card]):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().set_hand(cards)

    def has_card(self, card: Card):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().has_card(card)

    def remove_card(self, card: Card):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().remove_card(card)

    def has_quartet(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().has_quartet()

    def remove_all_quartet(self, callback):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        super().remove_all_quartet(callback)

    def has_cards(self):
        """
            This methods is overridden from the PlayerBase class.
            For more information take a look at the PlayerBase class.
        """
        return super().has_cards()
