import random

import time
from display import *
from sounds import *
from global_variables import next_cell

import time


# Checks whether or not the ship can be placed to the cell provided by either the user or the computer
def validate(board, ship, x, y, ori):
    # Check if the ship can be placed at given coordinates
    for next_x, next_y in next_cell:
        x_n = x + next_x
        y_n = y + next_y
        if ori == "v":
            if x_n + ship > 10:
                x_n = x
        if x_n < 0:
            x_n = 0
        elif x_n > 9:
            x_n = 9
        if ori == "h":
            if y_n + ship > 10:
                y_n = y
        if y_n < 0:
            y_n = 0
        elif y_n > 9:
            y_n = 9

        if ori == "v" and x + ship > 10:
            return False
        elif ori == "h" and y + ship > 10:
            return False
        else:
            if ori == "v":
                for i in range(ship):
                    if board[x_n + i][y_n] != "#":
                        return False
            elif ori == "h":
                for i in range(ship):
                    if board[x_n][y_n + i] != "#":
                        return False
    return True


# The function asking for player input regarding whether or not the ships should be placed vertically or horizontally.
def v_or_h():
    # Get ship orientation from user
    while(True):
        user_input = input("Would you like to place your ship vertically or horizontally? (v,h): ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print("Invalid input. Please only enter v or h!")


# Getting the coordinates from the user
def get_coor():
    valid = False
    while not valid:
        user_input = input("Please enter coordinates (row,col): ")
        try:
            # Ckeck if user entered 2 values seprated by comma
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            # Check that 2 values are integers
            coor[0] = int(coor[0]) - 1
            coor[1] = int(coor[1]) - 1

            # Check that values of integers are between 1 and 10 for both
            # coordinates
            if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                raise Exception(
                    "Invalid entry. Please use values between 1 to 10 only.")

            # If everything is ok, return coordinates
            return coor

        except ValueError:
            place_ship_sound()
            print("Try giving numbers.")
        except Exception as e:
            print(e)


# Placing ships to the board
def place_ship(board, ship_size, s, ori, x, y):

    # Place the ship based on orientation
    if ori == "v":
        for i in range(ship_size):
            board[x + i][y] = s
    elif ori == "h":
        for i in range(ship_size):
            board[x][y + i] = s

    place_ship_sound()


# Code for the computer placing ships
def computer_place_ships(board, ships, ships_data, player, player_2):
    for ship in ships:
        ship_size = ships[ship]
        valid = False
        while(not valid):

            x = random.randint(1, 10) - 1
            y = random.randint(1, 10) - 1
            o = random.randint(0, 1)

            if o == 0:
                ori = "v"
            else:
                ori = "h"

            valid = validate(board, ship_size, x, y, ori)

        # Place the ship
        print("\nThe Computer is placing a/an " + ship)
        place_ship(board, ship_size, ship_color(ship[0]), ori, x, y)

        row = []
        row.append([ship, ship_size])
        # Append coords to ships data
        if ori == "v":
            for s in range(ship_size):
                row.append([x + s, y])
            ships_data.append(row)
        elif ori == "h":
            for s in range(ship_size):
                row.append([x, y + s])
            ships_data.append(row)

        time.sleep(0.5)

    return board


# Asking for ship's coordinate from player
def user_place_ships(board, ships, ships_data, player, player_2):
    clear()
    print_board(player, player_2, board)
    print("\n" + player + " - Place your ship")
    for ship in ships:
        ship_size = ships[ship]
        # Get coordinates from user and validate the position
        valid = False
        while(not valid):

            print("\nPlacing a/an " + ship)
            x, y = get_coor()
            ori = v_or_h()

            valid = validate(board, ship_size, x, y, ori)

            if not valid:
                print("Cannot place a ship there.")
                print("The ships cannot be placed that close to each other.")
                print("Please take a look at the board and try again.")
                input("Hit ENTER to continue")
                clear()
                print_board(player, player_2, board)

        row = []
        row.append([ship, ship_size])
        # Append coords to ships data
        if ori == "v":
            for s in range(ship_size):
                row.append([x + s, y])
            ships_data.append(row)
        elif ori == "h":
            for s in range(ship_size):
                row.append([x, y + s])
            ships_data.append(row)

        # Place the ship
        place_ship(board, ship_size, ship_color(ship[0]), ori, x, y)
        clear()
        print_board(player, player_2, board)

    input("\nDone placing your ships. Hit ENTER to continue")
    clear()
    return board
