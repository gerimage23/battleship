import copy
import random

from display import *


def computer_place_ships(board, ships, ships_data):
    for ship in ships.keys():
        valid = False
        while(not valid):

            x = random.randint(1, 10) - 1
            y = random.randint(1, 10) - 1
            o = random.randint(0, 1)

            if o == 0:
                ori = "v"
            else:
                ori = "h"

            next_cell = [[i, j] for i in range(-1, 2)
                         for j in range(-1, 2) if abs(i + j) == 1]
            for n in next_cell:
                x_1 = x + n[0]
                y_1 = y + n[1]
                if x_1 < 0:
                    x_1 = 0
                if x_1 > 9:
                    x_1 = 9
                if y_1 < 0:
                    y_1 = 1
                if y_1 > 9:
                    y_1 = 9

                valid = validate(board, ships[ship], x_1, y_1, ori)

        # Place the ship
        print("\nThe Computer is placing a/an " + ship)
        board = place_ship(
            board, ships[ship], ship_color(ship[0]), ori, x, y)

        row = []
        row.append([ship, ships[ship]])
        # Append coords to ships data
        if ori == "v":
            for s in range(ships[ship]):
                row.append([x + s, y])
            ships_data.append(row)
        elif ori == "h":
            for s in range(ships[ship]):
                row.append([x, y + s])
            ships_data.append(row)
        # print(ships_data)
        input('\nPress ENTER to continue')

    return board


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


# Asking ship's coordinate from player
def user_place_ships(board, ships, ships_data):
    clear()
    print_board(board)
    print("\n" + player + " - Place your ship")
    for ship in ships.keys():

        # get coordinates from user and validate the postion
        valid = False
        while(not valid):

            # print_board(board)
            print("\nPlacing a/an " + ship)
            x, y = get_coor()
            ori = v_or_h()
            next_cell = [[i, j] for i in range(-1, 2)
                         for j in range(-1, 2) if abs(i + j) == 1]
            for n in next_cell:
                x_1 = x + n[0]
                y_1 = y + n[1]
                if x_1 < 0:
                    x_1 = 0
                if x_1 > 9:
                    x_1 = 9
                if y_1 < 0:
                    y_1 = 1
                if y_1 > 9:
                    y_1 = 9
                valid = validate(board, ships[ship], x_1, y_1, ori)
                # valid = validate(board, ships[ship], x, y, ori)
                if not valid:
                    print(
                        "Cannot place a ship there.\nThe ships cannot be placed that close to each other.\nPlease take a look at the board and try again.")
                    input("Hit ENTER to continue")
                    clear()
                    print_board(board)
                    break

        row = []
        row.append([ship, ships[ship]])
        # Append coords to ships data
        if ori == "v":
            for s in range(ships[ship]):
                row.append([x + s, y])
            ships_data.append(row)
        elif ori == "h":
            for s in range(ships[ship]):
                row.append([x, y + s])
            ships_data.append(row)

        # place the ship
        board = place_ship(board, ships[ship], ship_color(ship[0]), ori, x, y)
        clear()
        print_board(board)

    input("\nDone placing your ships. Hit ENTER to continue")
    clear()
    return board


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


def validate(board, ship, x, y, ori):
    # validate the ship can be placed at given coordinates
    if ori == "v" and x + ship > 10:
        return False
    elif ori == "h" and y + ship > 10:
        return False
    else:
        if ori == "v":
            for i in range(ship):
                if board[x + i][y] != "#":
                    return False
        elif ori == "h":
            for i in range(ship):
                if board[x][y + i] != "#":
                    return False
    return True


def v_or_h():

    # get ship orientation from user
    while(True):
        user_input = input("Vertical or horizontal (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print("Invalid input. Please only enter v or h")


def get_coor():
    valid = False
    while not valid:
        user_input = input("Please enter coordinates (row,col) ? ")
        try:
            # see that user entered 2 values seprated by comma
            coor = user_input.split(",")
            if len(coor) != 2:
                raise Exception("Invalid entry, too few/many coordinates.")

            # check that 2 values are integers
            coor[0] = int(coor[0]) - 1
            coor[1] = int(coor[1]) - 1

            # check that values of integers are between 1 and 10 for both
            # coordinates
            if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                raise Exception(
                    "Invalid entry. Please use values between 1 to 10 only.")

            # if everything is ok, return coordinates
            return coor

        except ValueError:
            print("Try giving numbers.")
        except Exception as e:
            print(e)


# Placing ships
def place_ship(board, ship, s, ori, x, y):

    # place ship based on orientation
    if ori == "v":
        for i in range(ship):
            board[x + i][y] = s
    elif ori == "h":
        for i in range(ship):
            board[x][y + i] = s

    return board


def check_win(board, ships_data):

    # if ships data is empty -> WIN
    # for i in range(10):
    #     for j in range(10):
    #         if board[i][j] != "#" and board[i][j] != green('x') and board[i][j] != red('0'):
    #             return False
    if ships_data:
        return False
    return True


# Choose your enemy
x_0 = 0
y_0 = 0
hit = 0
hit_again = 0
ai_i = 0
next_cell = [[1, 0], [0, 1], [-1, 0], [0, -1]]
direction = 1
valid = False

clear()
while not valid:
    userinput = input(
        "\nPlease select whether you are playing against another player or the computer(p or c): ")
    if userinput == "p":
        player_2 = "Player 2"
        valid = True
    if userinput == "c":
        player_2 = "Computer"
        valid = True
    else:
        print("Please select either c or p!")

# Generate the empty board
board = []
for i in range(10):
    board.append(['#'] * 10)

# Ships
ships = {"Aircraft Carrier": 5,
         "Battleship": 4,
         "Submarine": 3,
         "Destroyer": 3,
         "Patrol Boat": 2}

ships_data_1 = []
ships_data_2 = []

# setup players' boards
user_1_board = copy.deepcopy(board)
user_2_board = copy.deepcopy(board)

# add ships as last element in the array
user_1_board.append(copy.deepcopy(ships))
user_2_board.append(copy.deepcopy(ships))

# ship placement
player = "Player 1"
user_1_board = user_place_ships(user_1_board, ships, ships_data_1)
clear()
player = "Player 2"
if player_2 == "Player 2":
    user_2_board = user_place_ships(user_2_board, ships, ships_data_2)
else:
    player = "Computer"
    user_2_board = computer_place_ships(user_2_board, ships, ships_data_2)

# game begins
clear()
print(green("\nLet's play!"))
winner = 0
turn = 0
while not winner:
    turn += 1
    if turn % 2 != 0:
        player = "Player 1"
    else:
        player = player_2

    if player == "Player 1":
        board_you = user_1_board
        board_enemy = user_2_board
        ships_data = ships_data_2
    elif player == "Player 2" or player == "Computer":
        board_you = user_2_board
        board_enemy = user_1_board
        ships_data = ships_data_1

    print("\nTurn {}, {}".format(turn, player))

    # user move
    if player != "Computer":
        print_board(None, board_enemy)
        board_enemy = user_move(board_enemy, ships_data)

    # computer move
    if player == "Computer":
        if hit == 0:
            board_enemy = computer_move(board_enemy, ships_data)
        else:
            board_enemy = computer_ai(board_enemy, ships_data)


# winner?
    if board_enemy == "WIN":
        winner = player
    else:
        clear()

print("\n" + player + " won!!!\n")
