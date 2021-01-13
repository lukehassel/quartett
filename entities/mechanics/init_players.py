from entities.player.bot import Bot
from entities.player.user import User
from ui.ui_console_impl import UIConsoleImpl
from ui.ui_interface import UIInterface



def create_players(ui:UIInterface):

    liste = []
    number = int(input("Bitte geben Sie die Anzahl der Spieler ein: "))
    for i in range(number):
        player = input("Bitte geben Sie den Namen der Spieler an: ")
        value = int(input("Computerspieler = 0, player = 1: "))
        if value == 0:
            y = "Bot("" + player + "")"
            liste.append(y)
        elif value == 1:
            x = "User("" + player + "")"
            liste.append(x)
    print(liste)
    return liste
    create_players()