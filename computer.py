import random

from display import *
from user import check_win


def computer_move(board, ships_data, player, player_2):

    valid = False
    while not valid:
        x = random.randint(1, 10) - 1
        y = random.randint(1, 10) - 1

        board_cell = board[x][y]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == red('0') or board_cell == ship_color("0") or \
                board_cell == red('A') or board_cell == red('B') or board_cell == red('S') or \
                board_cell == red('D') or board_cell == red('P'):
            continue
        else:
            valid = True

    # checking
    if board_cell != "#":

        if board_cell == ship_color("A"):
            ship_name = "Aircraft Carrier"
        elif board_cell == ship_color("B"):
            ship_name = "Battleship"
        elif board_cell == ship_color("S"):
            ship_name = "Submarine"
        elif board_cell == ship_color("D"):
            ship_name = "Destroyer"
        elif board_cell == ship_color("P"):
            ship_name = "Patrol Boat"
        print("\nComputer hit a ship")
        board[x][y] = ship_color("0")

        globals.hit = 1
        globals.x_0 = x
        globals.y_0 = y

        # mark cell as hit and check if sunk
        board[-1][ship_name] -= 1
        if board[-1][ship_name] == 0:
            print("\nPlayer 1's" + ship_name + "sunk!")

            # Color ship to red
            for ship_data in ships_data:
                if ship_data[0][0] == ship_name:
                    for coords in ship_data[1:]:
                        i = coords[0]
                        j = coords[1]
                        board[i][j] = red(ship_data[0][0][0])
                    ships_data.remove(ship_data)
            print_board(player, player_2, None, board)

            # Check if this was the last ship -> WIN
            if check_win(board, ships_data):
                return "WIN"

            input('\nPress ENTER to continue')
            return
        print_board(player, player_2, None, board)
        input('\nPress ENTER to continue')
        return

    # Missed
    else:
        print("\nMissed.")
        board[x][y] = green("x")
        globals.hit = 0
    print_board(player, player_2, None, board)
    input('\nPress ENTER to continue')
    return board


def computer_ai(board, ships_data, player, player_2):

    if globals.hit_again == 0:
        globals.x_prev = globals.x_0
        globals.y_prev = globals.y_0

    valid = False
    while not valid:

        x = globals.x_prev + globals.next_cell[globals.ai_i][0] * globals.direction
        y = globals.y_prev + globals.next_cell[globals.ai_i][1] * globals.direction
        if x < 0 or x > 9 or y < 0 or y > 9:
            if globals.hit_again == 1:
                globals.direction *= -1
            else:
                globals.ai_i += 1
            continue
        board_cell = board[x][y]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == red('0') or board_cell == ship_color("0") or \
                board_cell == red('A') or board_cell == red('B') or board_cell == red('S') or \
                board_cell == red('D') or board_cell == red('P'):

            globals.x_prev = x
            globals.y_prev = y
            continue
        else:
            valid = True

    # checking
    if board_cell != "#":

        if board_cell == ship_color("A"):
            ship_name = "Aircraft Carrier"
        elif board_cell == ship_color("B"):
            ship_name = "Battleship"
        elif board_cell == ship_color("S"):
            ship_name = "Submarine"
        elif board_cell == ship_color("D"):
            ship_name = "Destroyer"
        elif board_cell == ship_color("P"):
            ship_name = "Patrol Boat"
        print("\nComputer hit a ship")
        board[x][y] = ship_color("0")
        globals.hit_again = 1
        globals.x_prev = x
        globals.y_prev = y

        # mark cell as hit and check if sunk
        board[-1][ship_name] -= 1
        if board[-1][ship_name] == 0:
            print("\nPlayer 1's " + ship_name + " sunk!")
            globals.hit = 0
            globals.hit_again = 0
            globals.ai_i = 0
            # Color ship to red
            for ship_data in ships_data:
                if ship_data[0][0] == ship_name:
                    for coords in ship_data[1:]:
                        i = coords[0]
                        j = coords[1]
                        # if board_enemy[i][j] == board_cell:
                        board[i][j] = red(ship_data[0][0][0])
                    ships_data.remove(ship_data)
            print_board(player, player_2, None, board)

            # Check if this was the last ship -> WIN
            if check_win(board, ships_data):
                return "WIN"

            input('\nPress ENTER to continue')
            return
        print_board(player, player_2, None, board)
        input('\nPress ENTER to continue')
        return

    # Missed
    else:
        print("\nMissed.")
        board[x][y] = green("x")

        if globals.hit_again == 1:
            globals.direction *= -1
        else:
            globals.ai_i += 1
    print_board(player, player_2, None, board)
    input('\nPress ENTER to continue')
    return board
