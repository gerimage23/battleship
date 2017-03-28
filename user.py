from display import *


def user_move(board, ships_data):
    # Ask a coordinate
    valid = False
    while not valid:
        user_input = input("\nGuess coordinates (row, col): ")
        try:
            # see that user entered 2 values seprated by comma
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            # check that 2 values are integers
            guess_row = int(coor[0]) - 1
            guess_col = int(coor[1]) - 1

            valid = True

        except ValueError:
            print("\nTry giving numbers.")

        except Exception as e:
            print(e)

    # Out of range
    if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
        print("\nOops, that's not even in the ocean.")
        input('\nPress ENTER to continue')
        return
    else:
        board_cell = board[guess_row][guess_col]
        # Is this cell a new one?

        if board_cell == green("x") or board_cell == red('0') or  board_cell == ship_color("0") or \
                board_cell == red('A') or board_cell == red('B') or board_cell == red('S') or \
                board_cell == red('D') or board_cell == red('P'):
            print("\nYou guessed that one already.")
            input('\nPress ENTER to continue')
            return

        # checking
        elif board_cell != "#":

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
            clear()
            print("\nYou hit a ship")
            board[guess_row][guess_col] = ship_color("0")

            # mark cell as hit and check if sunk
            board[-1][ship_name] -= 1
            if board[-1][ship_name] == 0:
                print("\n" + ship_name + " sunk!")

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
            clear()
            print("\nYou missed.")
            board[guess_row][guess_col] = green("x")
        print_board(None, board)
        input('\nPress ENTER to continue')


def check_win(board, ships_data):

    # if ships data is empty -> WIN
    # for i in range(10):
    #     for j in range(10):
    #         if board[i][j] != "#" and board[i][j] != green('x') and board[i][j] != red('0'):
    #             return False
    if ships_data:
        return False
    return True
