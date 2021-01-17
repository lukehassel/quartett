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
