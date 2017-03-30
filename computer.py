import random

from display import *
from user import check_win, ship_names, is_cell_not_empty, ship_color_to_red


def computer_move(board, ships_data, player, player_2):

    valid = False
    while not valid:
        x = random.randint(1, 10) - 1
        y = random.randint(1, 10) - 1

        board_cell = board[x][y]

        # Is this cell a new one?
        if is_cell_not_empty(board_cell):
            continue
        else:
            valid = True
    shoot_sound()
    # Checking hit
    if board_cell != "#":

        ship_name = ship_names(board_cell)
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
            ship_color_to_red(ships_data, ship_name, board)
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
        if is_cell_not_empty(board_cell):
            if global_variables.hit_again == 1:
                global_variables.direction *= -1
                global_variables.x_prev = global_variables.x_0
                global_variables.y_prev = global_variables.y_0
                continue
            else:
                global_variables.ai_i += 1
                continue
        else:
            valid = True

    # Checking hit
    if board_cell != "#":

        ship_name = ship_names(board_cell)
        print("\nComputer hit a ship")
        board[x][y] = ship_color("0")
        global_variables.hit_again = 1
        global_variables.x_prev = x
        global_variables.y_prev = y

        # Mark cell as hit and check if sunk
        board[-1][ship_name] -= 1
        if board[-1][ship_name] == 0:
            print("\nPlayer 1's " + ship_name + " sunk!")
            global_variables.hit = 0
            global_variables.hit_again = 0
            global_variables.ai_i = 0
            global_variables.direction = 1

            # Color ship to red
            ship_color_to_red(ships_data, ship_name, board)
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
