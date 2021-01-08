__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from abc import ABC, abstractmethod


class UIInterface(ABC):
    @abstractmethod
    def show_start_message(self):
        """
            A method which shows the start Message and informations on how to quit and restart the game.
        """
        pass