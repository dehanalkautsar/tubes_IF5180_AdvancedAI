import random

class Board(object):
    def __init__(self, size=10):
        self.size = size    
        self.board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.board_static = [[" " for _ in range(self.size)] for _ in range(self.size)]
        
    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 1))

    def init_board(self, player, listWumpus, gold):
        #display board
        self.board[player.x][player.y] = "P"
        for wumpus in listWumpus:
            self.board[wumpus.x][wumpus.y] = "W"
            self.add_stench(wumpus)
        self.board[gold.x][gold.y] = "G"

        #static board
        for wumpus in listWumpus:
            self.board_static[wumpus.x][wumpus.y] = "W"
            self.add_stench_static(wumpus)
        self.board_static[gold.x][gold.y] = "G"
        

    def add_stench(self, wumpus):
        if wumpus.x > 0 and self.board[wumpus.x-1][wumpus.y] == " ":
            self.board[wumpus.x-1][wumpus.y] = "~"
        if wumpus.x < self.size-1 and self.board[wumpus.x+1][wumpus.y] == " ":
            self.board[wumpus.x+1][wumpus.y] = "~"
        if wumpus.y > 0 and self.board[wumpus.x][wumpus.y-1] == " ":
            self.board[wumpus.x][wumpus.y-1] = "~"
        if wumpus.y < self.size-1 and self.board[wumpus.x][wumpus.y+1] == " ":
            self.board[wumpus.x][wumpus.y+1] = "~"

    def add_stench_static(self, wumpus):
        if wumpus.x > 0 and self.board_static[wumpus.x-1][wumpus.y] == " ":
            self.board_static[wumpus.x-1][wumpus.y] = "~"
        if wumpus.x < self.size-1 and self.board_static[wumpus.x+1][wumpus.y] == " ":
            self.board_static[wumpus.x+1][wumpus.y] = "~"
        if wumpus.y > 0 and self.board_static[wumpus.x][wumpus.y-1] == " ":
            self.board_static[wumpus.x][wumpus.y-1] = "~"
        if wumpus.y < self.size-1 and self.board_static[wumpus.x][wumpus.y+1] == " ":
            self.board_static[wumpus.x][wumpus.y+1] = "~"

        
    def update_board(self, x, y, symbol):
        self.board[x][y] = symbol
        

class Wumpus(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Gold(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.num_movement = 0
        self.percept = {
            "stench" : False
        }

    def move(self, board, direction):
        board.update_board(self.x, self.y, board.board_static[self.x][self.y])
          
        if direction=="W" and self.x > 0:
            self.x = self.x-1
        elif direction=="A" and self.y > 0:
            self.y = self.y - 1
        elif direction=="S" and self.x < board.size:
            self.x = self.x + 1
        elif direction=="D" and self.y < board.size:
            self.y = self.y+1

        board.update_board(self.x, self.y, "P")
        self.percept["stench"] = board.board_static[self.x][self.y] == "~"

    def is_finished(self, listWumpus, gold):
        for wumpus in listWumpus:
            if self.x == wumpus.x and self.y == wumpus.y:
                print("======================\nAnda kalah 😭")
                return True
        if self.x == gold.x and self.y == gold.y:
            print("======================\nSelamat, Anda menang 😄")
            return True
        return False

def movement():
    while True:
        move = input("masukkan gerakan: ").upper()
        if move in ["W", "A", "S", "D"]:
            break

    return move

def main():
    # Print header
    print("⭐⭐SELAMAT DATANG DI PERMAINAN WUMPUS⭐⭐")

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
        print("Jumlah pergerakan pemain:", myPlayer.num_movement)
        print("Persepsi pemain:", myPlayer.percept)
        dir = movement()
        myPlayer.num_movement += 1
        myPlayer.move(myBoard, dir)
        
        if myPlayer.is_finished(listWumpus, gold):
            break
main()
    
