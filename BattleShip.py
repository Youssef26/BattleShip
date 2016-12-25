from random import randint
win1 = False
win2 = False
score1 = 0
score2 = 0
board = []
board1 = []
width = int(raw_input("Board Width: "))
height = int(raw_input("Board Height:"))
turns = int(raw_input("How many turns do you want to play? "))

for x in range(height):
    board.append(["O"] * width)
for x in range(height):
    board1.append(["O"] * width)
def print_board(board):
    for row in board:
        print " ".join(row)
players  = int(raw_input("1 or 2 players?"))
if players == 1:
    print "Let's play Battleship!"
    print_board(board)
else:
    print "Player 1 starts!"
    print_board(board)
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    # type: (object) -> object
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
carrier_row1 = random_row(board)
carrier_col1 = random_col(board)
carrier_row2 = carrier_row1 - 1
if carrier_row2 < 0 or carrier_row1 == 0:
    carrier_row1 += 1
    carrier_row2 += 1
while (carrier_row1 or carrier_row2 == ship_row) and (carrier_col1 == ship_col):
    if carrier_col1 >= 0:
        carrier_col1 -= 1
print ship_row
print ship_col
print carrier_row1
print carrier_row2
print carrier_col1
for turn1 in range(turns):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if (guess_row == ship_row and guess_col == ship_col) or ((guess_col == carrier_col1) and guess_row == (carrier_row2 or carrier_row2)):
        print "Congratulations! You hit a battleship!"
        board[guess_row][guess_col] = "1"
        score1 += 1
    else:
        if (guess_row < 0 or guess_row > len(board) - 1) or (guess_col < 0 or guess_col > len(board) - 1):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        elif board[guess_row][guess_col] ==  "1":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    print "Turn ", turn1 +1
    print_board(board)
print "Game Over!"
"""if players != 1:
    print "Player 2 starts now!"
    ship_row = random_row(board1)
    ship_col = random_col(board1)
    carrier_row1 = random_row(board1)
    carrier_col1 = random_col(board1)
    carrier_row2 = carrier_row1 - 1
    while carrier_row2 < 0 or carrier_col1 < 0:
        carrier_row1 += 1
        carrier_row2 += 1
        carrier_col1 += 1
    print ship_row
    print ship_col
    print carrier_row1
    print carrier_row2
    print carrier_col1
    for turn2 in range(turns):
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        if (guess_row == ship_row and guess_col == ship_col) or (guess_col == carrier_col1) and (
                guess_row == carrier_row2 or carrier_row2):
            print "Congratulations! You hit a battleship!"
            board1[guess_row][guess_col] = "2"
            score2 += 1
        else:
            if (guess_row < 0 or guess_row > len(board1) - 1) or (guess_col < 0 or guess_col > len(board1) - 1):
                print "Oops, that's not even in the ocean."
            elif board1[guess_row][guess_col] == "2" or board1[guess_row][guess_col] == "X":
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board1[guess_row][guess_col] = "X"
        print "Turn ", turn2 + 1
        print_board(board1)
    if turn2 == 2:
        print "Game Over!"
    if score1 == score2:
        "Draw, everyone wins! :D"
    elif score1 > score2:
        print "player 1 wins!"
    elif score2 > score1:
        print "player 2 wins!"""""