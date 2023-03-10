

import random

# ---------- Input welcome to start the game and assign each symbol -----------
print("\nāā­ WELCOME TO TICTACTOE GAME ā­ā\n")
print("RULES: š\nš¹ The game is played on a grid that's 3 squares by 3 squares.\nš¹ One player plays with X and the other with O, by random assignment.\nš¹ There is no universally-agreed rule as to who plays first, but in this 'pygame' X plays first. \nš¹ Players take turns putting their marks ONLY in empty squares, else lose the turn.\nš¹ The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\nš¹ When all 9 squares are full, the game is over.\n")

player1_name = input("š¾ Player1 enter your name: ")
player2_name = input("š½ Player2 enter your name: ")
player1 = random.randint(0, 1)

if player1:
    print(f"\n{player1_name}, you will play with crosses ā")
    print(f"{player2_name}, you will play with noughts ā­\n")
    crosses_player = player1_name
else:
    print(f"\n{player1_name}, you will play with noughts ā­")
    print(f"{player2_name}, you will play with crosses ā\n")
    crosses_player = player2_name

# ------------------------- Create and print the grid -------------------------
GRID_SQUARES = ["0ļøā£ ", "1ļøā£ ", "2ļøā£ ", "3ļøā£ ", "4ļøā£ ", "5ļøā£ ", "6ļøā£ ", "7ļøā£ ", "8ļøā£ "]
SQUARE_SIZE = len(GRID_SQUARES) ** 0.5
i = 0
row = []
grid = []

for square in GRID_SQUARES:
    row.append(square)
    i += 1
    if i % SQUARE_SIZE == 0:
        row = " | ".join(row)
        grid.append(row)
        row = []
grid = "\nāāāāāāāāāāāāā\n".join(grid)
print(grid)
print(f"\nCrosses(ā) start so {crosses_player} you first ā”")

# ------------------------------------ GAME -----------------------------------
turn = True
crosses = []
noughts = []
have_a_winner = False
grid = []
WINNING_SQUARES = [[0, 1, 2],[0, 4, 8],[0, 3, 6],[2, 5, 8],[1, 4, 7],[6, 7, 8],[3, 4, 5],[2, 4, 6]]

for _ in GRID_SQUARES:
    if have_a_winner:
        break
    selected_square = int(input("\nEnter a number[0-8]: "))
    while selected_square >= len(GRID_SQUARES) or selected_square < 0:
        selected_square = int(input("š¢ Grrrr!!!š¾ Enter a number between 0 and 8! Try again š»:\n"))
    if GRID_SQUARES[(selected_square)] == "ā" or GRID_SQUARES[(selected_square)] == "ā­":
        selected_square = "š©"
        print("ā Error: You're trying to mark in a filled square!š· Sorry, but you lose your turn!š\n")
    if turn:
        symbol = "ā"
        turn = False
        crosses.append(selected_square)
    else:
        symbol = "ā­"
        turn = True
        noughts.append(selected_square)
    if selected_square != "š©":
        GRID_SQUARES[(selected_square)] = symbol

    # ------------------------ Check out the winner -------------------------
    crosses_in_row, noughts_in_row = 0, 0
    for win_combi in WINNING_SQUARES:
        crosses_in_row, noughts_in_row = 0, 0
        for num in win_combi:
            if num in crosses:
                crosses_in_row += 1
            if num in noughts:
                noughts_in_row += 1
        if crosses_in_row == SQUARE_SIZE or noughts_in_row == SQUARE_SIZE:
            have_a_winner = True
            break

    # ---------------------------- Print the grid -----------------------------
    i = 0
    for square in GRID_SQUARES:
        row.append(square)
        i += 1
        if i % SQUARE_SIZE == 0:
            row = " | ".join(row)
            grid.append(row)
            row = []
    grid = "\nāāāāāāāāāāāāā\n".join(grid)
    print()
    print(grid)
    grid = []
# ----------------------------- Who win the game ------------------------------
if have_a_winner:
    print(f"\n{symbol} Ā”WIN! š Well done. š")
else:
    print("\nNo one wins! šæ")
# -----------------------------------------------------------------------------
"""---------------------- TicTacToe2.0 n x n in progres...----------------------
import sys
n = int(sys.argv[1])
values = [i for i in range(n * n)]
grid_squares = [(values[i : i + n]) for i in range(len(values) - n + 1) if i % n == 0]
values = [(grid_squares[j][i]) for i in range(0, n) for j in range(0, n)]
for i in range(0, n):
    values.append(i * (n + 1))
for i in range(0, n):
    values.append((i + 1) * (n - 1))
winning_combinations = [values[i : i + n] for i in range(len(values) - n + 1) if i % n == 0]
"""