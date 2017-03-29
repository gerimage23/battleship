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

        if board_cell == green("x") or board_cell == ship_color("0") or \
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

        global_variables.hit = 1
        global_variables.x_0 = x
        global_variables.y_0 = y

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
        global_variables.hit = 0
    print_board(player, player_2, None, board)
    input('\nPress ENTER to continue')
    return board


def computer_ai(board, ships_data, player, player_2):

    if global_variables.hit_again == 0:
        global_variables.x_prev = global_variables.x_0
        global_variables.y_prev = global_variables.y_0

    valid = False
    while not valid:

        x = global_variables.x_prev + global_variables.next_cell[global_variables.ai_i][0] * global_variables.direction
        y = global_variables.y_prev + global_variables.next_cell[global_variables.ai_i][1] * global_variables.direction
        if x < 0 or x > 9 or y < 0 or y > 9:
            if global_variables.hit_again == 1:
                global_variables.direction *= -1
            else:
                global_variables.ai_i += 1
            continue
        board_cell = board[x][y]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == ship_color("0") or \
                board_cell == red('A') or board_cell == red('B') or board_cell == red('S') or \
                board_cell == red('D') or board_cell == red('P'):

            # global_variables.x_prev = x
            # global_variables.y_prev = y
            global_variables.ai_i += 1
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
        global_variables.hit_again = 1
        global_variables.x_prev = x
        global_variables.y_prev = y

        # mark cell as hit and check if sunk
        board[-1][ship_name] -= 1
        if board[-1][ship_name] == 0:
            print("\nPlayer 1's " + ship_name + " sunk!")
            global_variables.hit = 0
            global_variables.hit_again = 0
            global_variables.ai_i = 0
            global_variables.direction = 1
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

        if global_variables.hit_again == 1:
            global_variables.direction *= -1
        else:
            global_variables.ai_i += 1
    print_board(player, player_2, None, board)
    input('\nPress ENTER to continue')
    return board
