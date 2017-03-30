ships = {"Aircraft Carrier": 5,
         "Battleship": 4,
         "Submarine": 3,
         "Destroyer": 3,
         "Patrol Boat": 2
         }

# Computer AI variables:
#
# The origo coordinates after a ship hit to shoot it around and find its orientation
x_0 = 0
y_0 = 0

# After random shooting, if computer hit a ship, its value changes to 1
hit = 0

# When computer is shooting around and hit the ship again so it finds the orientation of ship, its value changes to 1
hit_again = 0

# The matrix to shoot around the origo after a ship hit
next_cell = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# Index of the matrix. Its value grow by 1 until computer not hit again
ai_i = 0

# The multiplexer of the next cell computing expression. Its value changes
# to -1 if computer find the end of the ship but not it has not been sunk
direction = 1
