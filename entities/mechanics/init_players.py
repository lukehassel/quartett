from entities.player.bot import Bot
from entities.player.user import User
from ui.ui_console_impl import UIConsoleImpl
from ui.ui_interface import UIInterface


# def create_players(self):
#     if gegner == 1:
#         bot()
#         pass
#     else:
#         player = int(input("Geben Sie Anzahl der Spieler an: "))
#         if player <= 2 or player > 8:
#             print("Versuchen Sie bitte nochmal")
#             user_Interface()
#         while counter < player:
#             player_name = str(input("Wie heißen Sie: "))
#             counter += 1
#             name_list.append(player_name)


def create_players(ui: UIConsoleImpl):
    return [User("fsaf"), Bot("adf"), User("fsaf")]
