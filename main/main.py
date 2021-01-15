from domain.usecase.game_usecase import GameUseCase
from ui.factory.ui_console_factory import UIConsoleFactory

if __name__ == '__main__':
    """
            This method starts the program.
    """

    console_ui = UIConsoleFactory().initUI()

    GameUseCase(console_ui).start_game()
