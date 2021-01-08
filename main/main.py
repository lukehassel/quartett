if __name__ == '__main__':
    print("hello world")
    print("test")
import os
import time
def welcome() :
    print("###################"),time.sleep(0.5)
    print("Wellcomen zum Spiel"),time.sleep(0.5)
    print("###################"),time.sleep(0.5)
welcome()
def user_Interface():
    """
    """
    counter = 0
    name_list = []
    print("Es dürfen min 3 bis 8 spieler zussamenspielen."),time.sleep(0.5)
    gegner = int(input("Geben Sie [1] für Bot oder [2] für Mensch: "))
    if gegner == 1:
        bot()
        pass
    else:
        player = int(input("Geben Sie Anzahl der Spieler an: "))
        if player <= 2 or player > 8:
            print("Versuchen Sie bitte nochmal")
            user_Interface()
        while counter < player:
            player_name = str(input("Wie heißen Sie: "))
            counter += 1
            name_list.append(player_name)
        print(name_list)
user_Interface()