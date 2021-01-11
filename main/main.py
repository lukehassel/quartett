from entities.mechanics.game_mechanics import GameMechanics
from ui.factory.ui_console_factory import UIConsoleFactory

if __name__ == '__main__':
    """
            This method starts the program.
    """

    console_ui = UIConsoleFactory().initUI()

    GameMechanics(console_ui).start_game()
