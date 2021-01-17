__author__ = "6966753, Khalil, 7340644, Hassel"
__email__ = "s7114097@stud.uni-frankfurt.de, s8911049@rz.uni-frankfurt.de"

from domain.entities.player.bot import Bot
from domain.entities.player.user import User
from ui.states.game_states import PlayerDidCreatePlayerList
from ui.ui_interface import UIInterface


def create_players(ui: UIInterface):
    """
    Creates the players.

    :param ui: The ui Interface.
    :return: A list of players generated form the ui.
    """
    p = ui.show_choose_players()
    if isinstance(p, PlayerDidCreatePlayerList):
        return p.players


