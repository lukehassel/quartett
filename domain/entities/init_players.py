from domain.entities.player.bot import Bot
from domain.entities.player.user import User
from ui.states.game_states import PlayerDidCreatePlayerList
from ui.ui_interface import UIInterface


def create_players(ui: UIInterface):
    p = ui.show_choose_players()
    if isinstance(p, PlayerDidCreatePlayerList):
        return p.players


