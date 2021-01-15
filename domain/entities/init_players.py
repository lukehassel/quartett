from domain.entities.player.bot import Bot
from domain.entities.player.user import User
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


def create_players(ui: UIInterface):
    return [Bot("aaaaa"), Bot("bbbbb"), User("cccccc")]

def players():
    liste = []
    number = int(input("Bitte geben Sie die Anzahl der Spieler ein: "))
    for i in range(number):
        player = input("Bitte geben Sie den Namen der Spieler an: ")
    print(liste)
    return liste

def bot_or_player(player: str, liste: [PlayerBase]):
    value = int(input("Computerspieler = 0, player = 1: "))
    if value == 0:
        y = Bot(player)
        liste.append(y)
    elif value == 1:
        x = User(player)
        liste.append(x)
    else:
