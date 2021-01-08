__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

import time

from ui.ui_interface import UIInterface


class UIConsoleImpl(UIInterface):
    """
        This is the UI console Implementation. All methods are overridden from UIInterface.
    """

    def show_start_message(self):
        """
            For more information about on what this method is implementing take a look at the UIInterface.
        """
        print("###################"), time.sleep(0.5)
        print("Willkommen zum Spiel"), time.sleep(0.5)
        print("###################"), time.sleep(0.5)

        print("Es dürfen min 3 bis max 8 spieler zusammenspielen."), time.sleep(0.5)

    def show_option_bot_or_user(self):
        opponent = int(input("Geben Sie [1] für Bot oder [2] für Mensch: "))
        if(opponent == 1):
