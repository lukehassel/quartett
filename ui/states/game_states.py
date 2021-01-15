__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.cards.card import Card
from domain.entities.player.player_base import PlayerBase


class GameState:
    """
        This class is the parent class of all the states in the game.
        For more information on the states take a look below.
    """
    pass


class GameInitialState(GameState):
    """
        This class represents a state in which the game can be.
        The GameInitialState is called at the beginning of the game.
    """
    pass


class GameNewRoundState(GameState):
    """
        This class represents a state in which the game can be.
        ...
    """
    pass


class GameExitState(GameState):
    """
        This class represents a state in which the game can be.
        ...
    """
    pass


class AskPlayerForCardAndPlayer(GameState):
    """
        This class represents a state in which the game can be.
        ...
    """

    def __init__(self, player: PlayerBase, card: Card):
        self.player = player
        self.card = card


class PlayerDidCreatePlayerList(GameState):

    def __init__(self, players: [PlayerBase]):
        self.players = players
