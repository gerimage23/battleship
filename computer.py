import random

from display import clear
from user import check_win


def computer_move(board, ships_data):
    valid = False
    while not valid:
        x = random.randint(1, 10) - 1
        y = random.randint(1, 10) - 1

        board_cell = board_enemy[x][y]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == red('0') or  board_cell == ship_color("0") or \
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
        board_enemy[x][y] = ship_color("0")
        global hit
        hit = 1
        global x_0
        x_0 = x
        global y_0
        y_0 = y

        # mark cell as hit and check if sunk
        board_enemy[-1][ship_name] -= 1
        if board_enemy[-1][ship_name] == 0:
            print("\nPlayer 1's" + ship_name + "sunk!")

            # Color ship to red
            for ship_data in ships_data:
                if ship_data[0][0] == ship_name:
                    for coords in ship_data[1:]:
                        i = coords[0]
                        j = coords[1]
                        # if board_enemy[i][j] == board_cell:
                        board_enemy[i][j] = red(ship_data[0][0][0])
                    ships_data.remove(ship_data)
            print_board(None, board_enemy)

            # Check if this was the last ship -> WIN
            if check_win(board_enemy, ships_data):
                return "WIN"

            input('\nPress ENTER to continue')
            return
        print_board(None, board_enemy)
        input('\nPress ENTER to continue')
        return

    # Missed
    else:
        print("\nMissed.")
        board_enemy[x][y] = green("x")
        global hit
        hit = 0
    print_board(None, board_enemy)
    input('\nPress ENTER to continue')
    return board


def computer_ai(board, ships_data):
    global ai_i
    global x_prev
    global y_prev
    global hit
    global x_0
    global y_0
    global hit_again
    global direction
    global next_cell

    if hit_again == 0:
        x_prev = x_0
        y_prev = y_0

    valid = False
    while not valid:

        x = x_prev + next_cell[ai_i][0] * direction
        y = y_prev + next_cell[ai_i][1] * direction
        if x < 0 or x > 9 or y < 0 or y > 9:
            if hit_again == 1:
                direction *= -1
            else:
                ai_i += 1
            continue
        board_cell = board[x][y]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == red('0') or  board_cell == ship_color("0") or \
                board_cell == red('A') or board_cell == red('B') or board_cell == red('S') or \
                board_cell == red('D') or board_cell == red('P'):

            x_prev = x
            y_prev = y
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
        hit_again = 1
        x_prev = x
        y_prev = y

        # mark cell as hit and check if sunk
        board[-1][ship_name] -= 1
        if board[-1][ship_name] == 0:
            print("\nPlayer 1's " + ship_name + " sunk!")
            hit = 0
            hit_again = 0
            ai_i = 0
            # Color ship to red
            for ship_data in ships_data:
                if ship_data[0][0] == ship_name:
                    for coords in ship_data[1:]:
                        i = coords[0]
                        j = coords[1]
                        # if board_enemy[i][j] == board_cell:
                        board[i][j] = red(ship_data[0][0][0])
                    ships_data.remove(ship_data)
            print_board(None, board)

            # Check if this was the last ship -> WIN
            if check_win(board, ships_data):
                return "WIN"

            input('\nPress ENTER to continue')
            return
        print_board(None, board)
        input('\nPress ENTER to continue')
        return

    # Missed
    else:
        print("\nMissed.")
        board[x][y] = green("x")

        if hit_again == 1:
            direction *= -1
        else:
            ai_i += 1
    print_board(None, board)
    input('\nPress ENTER to continue')
    return board
