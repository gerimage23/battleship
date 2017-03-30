from display import *
from sounds import *


# Defines the letters corresponding to the relevant ships
def ship_names(board_cell):
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
    return ship_name


# Changes the sunk ship color's to red
def ship_color_to_red(ships_data, ship_name, board):
    ship_sunk_sound()
    for ship_data in ships_data:
        if ship_data[0][0] == ship_name:
            for coords in ship_data[1:]:
                i = coords[0]
                j = coords[1]
                board[i][j] = red(ship_data[0][0][0])
            ships_data.remove(ship_data)


# Checks whether or not the targeted cell is reserved
def cell_is_reserved(board_cell):
    if board_cell == green("x") or board_cell == ship_color("0") or \
            board_cell == red('A') or board_cell == red('B') or \
            board_cell == red('S') or board_cell == red('D') or board_cell == red('P'):
        return True
    return False


# Code for the user shots on the board
def user_move(board, ships_data, player, player_2):
    # Ask for a coordinate
    valid = False
    while not valid:
        user_input = input("\nGuess coordinates (row, col): ")
        try:
            # Ckeck if the user entered 2 values seprated by comma
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            # Check that 2 values are integers
            guess_row = int(coor[0]) - 1
            guess_col = int(coor[1]) - 1

            valid = True

        except ValueError:
            print("\nTry giving numbers.")

        except Exception as e:
            print(e)

    # Out of range
    if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
        wrong_coords_sound()
        print("\nOops, that's not even in the ocean.")
        input('\nPress ENTER to continue')
        return
    else:
        board_cell = board[guess_row][guess_col]

        # Is this cell a new one?
        if cell_is_reserved(board_cell):
            wrong_coords_sound()
            print("\nYou guessed that one already.")
            input('\nPress ENTER to continue')
            return

        # Checking hit
        elif board_cell != "#":
            # Get ship_name from the hit cell
            ship_name = ship_names(board_cell)
            clear()
            hit_sound()
            print("\nYou hit a ship")
            board[guess_row][guess_col] = ship_color("0")

            # Mark cell as hit and check if sunk
            board[-1][ship_name] -= 1
            if board[-1][ship_name] == 0:
                print("\n" + ship_name + " sunk!")

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
            clear()
            shoot_sound()
            print("\nYou missed.")
            board[guess_row][guess_col] = green("x")
        print_board(player, player_2, None, board)
        input('\nPress ENTER to continue')


# Checks if the winning condition has been met or not
def check_win(board, ships_data):
    if ships_data:
        return False
    return True
