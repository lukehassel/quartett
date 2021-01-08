__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"


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


class ChooseBotOrUserState(GameState):
    """
        This class represents a state in which the game can be.
        ...
    """

    def __init__(self, isBot: bool):
        self.isBot = isBot
