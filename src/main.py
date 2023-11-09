import random

from board import *
from gold import *
from player import *
from wumpus import *
from movement import *

def main():
    # Print header
    print("⭐⭐WELCOME TO IF5080 SIMPLE WUMPUS WORLD⭐⭐")

    # Set board and player
    board_size = 10
    myBoard = Board(board_size)
    myPlayer = Player()

    # create wumpuses
    listWumpus = []
    wumpusPoint = []
    while len(listWumpus) < 3:
        point = [random.randint(2, board_size - 1), random.randint(2, board_size - 1)]
        if point not in wumpusPoint:
            wumpusPoint.append(point)
            wumpus = Wumpus(point[0], point[1])
            listWumpus.append(wumpus)

    #create gold
    while True:
        goldPoint = [random.randint(7, board_size - 1), random.randint(4, board_size - 1)]
        if goldPoint not in wumpusPoint:
            gold = Gold(goldPoint[0], goldPoint[1])
            break

    myBoard.init_board(myPlayer, listWumpus, gold)

    while True:
        print()
        myBoard.print_board()
        print("Number of player moves:", myPlayer.num_movement)
        print("Player perception:", myPlayer.percept)
        dir = movement(myPlayer)
        myPlayer.num_movement += 1
        myPlayer.move(myBoard, dir)

        if myPlayer.is_finished(listWumpus, gold):
            break
main()