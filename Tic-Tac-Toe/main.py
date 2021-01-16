# constants
NOUGHT = "O"
CROSS = "X"
EMPTY = "_"

NOUGHT_WIN = [NOUGHT, NOUGHT, NOUGHT]
CROSS_WIN = [CROSS, CROSS, CROSS]

# reading input
cells = list(input("Enter cells:"))

# print current game state
print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[8], "|")
print("---------")

# extract rows, columns and diagonals
triples = [
    # rows
    cells[:3],
    cells[3:6],
    cells[6:],
    # columns
    [cells[0], cells[3], cells[6]],
    [cells[1], cells[4], cells[7]],
    [cells[2], cells[5], cells[8]],
    # diagonals
    [cells[0], cells[4], cells[8]],
    [cells[6], cells[4], cells[2]]
]

# process game state
if cells.count(NOUGHT) - cells.count(CROSS) not in (1, 0, -1):
    # to much NOUGHTS or CROSSES
    print("Impossible")
elif (NOUGHT_WIN in triples) and (CROSS_WIN in triples):
    # NOUGHTS and CROSSES can't both wins
    print("Impossible")
elif NOUGHT_WIN in triples:
    print("O wins")
elif CROSS_WIN in triples:
    print("X wins")
elif EMPTY in cells:
    print("Game not finished")
else:
    # Nobody wins
    print("Draw")

