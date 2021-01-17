__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.usecase.game_usecase import GameUseCase
from ui.factory.ui_console_factory import UIConsoleFactory


def startProgram(debug=False):
    """
        This methods configures the ui and starts the game with the GameUseCase.
    """
    console_ui = UIConsoleFactory().initUI(debug)

    GameUseCase(console_ui)


if __name__ == '__main__':
    """
            The main method.
    """
    startProgram()
