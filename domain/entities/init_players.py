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


