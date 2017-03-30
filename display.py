
import copy
from subprocess import call
import time
import vlc

import global_variables


def shoot_sound():
    s = vlc.MediaPlayer("sounds/shoot.wav")
    s.play()


def clear():
    call('clear')
    print('''.______        ___   .___________.___________. __       _______     _______. __    __   __  .______      
|   _  \      /   \  |           |           ||  |     |   ____|   /       ||  |  |  | |  | |   _  \     
|  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__     |   (----`|  |__|  | |  | |  |_)  |    
|   _  <    /  /_\  \    |  |        |  |     |  |     |   __|     \   \    |   __   | |  | |   ___/     
|  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____.----)   |   |  |  |  | |  | |  |         
|______/  /__/     \__\  |__|        |__|     |_______||_______|_______/    |__|  |__| |__| | _|         
                                                                                                         ''')


def print_board(player, player_2, board_you=None, board_enemy=None):
    ships = global_variables.ships
    if board_you:
        if player != "Computer":
            print('\n' + player + "'s board")
            print('\n   ', end='')
            for i in range(1, 11):
                print(i, end=' ')
            print('')
            for i, j in enumerate(board_you):
                if i > 9:
                    break
                print("{0:2d} {1}".format(i + 1, " ".join(j)))

    if board_enemy:
        if player_2 == "Computer" and player != player_2:
            print('\nComputer\'s board')
        elif player != "Computer":
            print('\nEnemy\'s board')
        print('\n   ', end='')
        for i in range(1, 11):
            print(i, end=' ')
        print('')
        letters = [ship_color(ship[0]) for ship in ships.keys()]
        for i, j in enumerate(board_enemy):
            if i > 9:
                break
            j_hidden = copy.deepcopy(j)
            for x in range(10):
                if j_hidden[x] in letters:
                    j_hidden[x] = "#"
            print("{0:2d} {1}".format(i + 1, " ".join(j_hidden)))


def red(string):
    # Change the color of the string to red
    char = "\033[91m" + string + "\033[00m"
    return char


def green(string):
    # Change the color of the string to green
    char = '\x1b[6;30;42m' + string + '\x1b[0m'
    return char


def ship_color(string):
    # Change the color of the ship
    char = '\x1b[1;34;40m' + string + '\x1b[0m'
    return char
