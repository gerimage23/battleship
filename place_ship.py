import random


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
