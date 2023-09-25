import random

BOARD_SIZE = 10

# Inisiasi papan permainan
board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

wumpus_location = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
gold_location = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))

#  Fungsi untuk memperbarui posisi pemain, wumpus, dan emas
def initialize_board():
    board[wumpus_location[0]][wumpus_location[1]] = "W"
    board[gold_location[0]][gold_location[1]] = "G"
    board[player_location[0]][player_location[1]] = "P"

# Fungsi untuk mencetak papan permainan
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (BOARD_SIZE * 4 - 1))

# Fungsi untuk memeriksa apakah pemain menang atau kalah
def check_status(player_location):
    if player_location == wumpus_location:
        return "Kalah! Kamu digigit oleh Wumpus."
    elif player_location == gold_location:
        return "Menang! Kamu menemukan emas!"
    else:
        return "Berlanjut..."
    
# Fungsi move
def movement():
    direction = input("Masukkan langkah (W/A/S/D): ")
    return direction

# Fungsi bergerak
def update_player_position(move):
    board[player_location[0]][player_location[1]] = " "

    if move == "W" and player_location[0] > 0:
        player_location = (player_location[0] - 1, player_location[1])
    elif move == "A" and player_location[1] > 0:
        player_location = (player_location[0], player_location[1] - 1)
    elif move == "S" and player_location[0] < BOARD_SIZE - 1:
        player_location = (player_location[0] + 1, player_location[1])
    elif move == "D" and player_location[1] < BOARD_SIZE - 1:
        player_location = (player_location[0], player_location[1] + 1)

    board[player_location[0]][player_location[1]] = "P"

def main():
    global player_location
    player_location = (0,0)
    initialize_board()
    while True:
        print_board(board)
        print(check_status(player_location))

        move = movement()

        update_player_position(move)


main()