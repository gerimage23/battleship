import copy

from display import *
from place_ship import *
from computer import *


def main():
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

if __name__ == '__main__':
    main()
