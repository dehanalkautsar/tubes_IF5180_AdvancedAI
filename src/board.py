import random

class Board(object):
    def __init__(self, size=10):
        self.size = size    
        self.board = [[[] for _ in range(self.size)] for _ in range(self.size)]
        
    def print_board(self):
        for row in self.board:
            print("|", end="")
            for mem in row:
                if (len(mem) == 0):
                    print("    |", end="")
                else:
                    print("".join(mem)+(4-len(mem))*" "+"|", end="")
            print()
            print("-" * ((self.size) * 5))

    def init_board(self, player, wumpus, gold):
        self.board[player.x][player.y].append("P")
        self.board[wumpus.x][wumpus.y].append("W")
        self.add_stench(wumpus)
        self.board[gold.x][gold.y].append("G")
        

    def add_stench(self, wumpus):
        if wumpus.x > 0:
            self.board[wumpus.x-1][wumpus.y].append("~")
        if wumpus.x < self.size-1:
            self.board[wumpus.x+1][wumpus.y].append("~")
        if wumpus.y > 0:
            self.board[wumpus.x][wumpus.y-1].append("~")
        if wumpus.y < self.size-1:
            self.board[wumpus.x][wumpus.y+1].append("~")

        
    def update_board(self, x, y, symbol, delete=False):
        if delete:
            self.board[x][y].remove(symbol)
        else:
            self.board[x][y].append(symbol)
        

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

    def move(self, board, direction, wumpus):
        board.update_board(self.x, self.y, "P")
        board.add_stench(wumpus)
        if direction=="W" and self.x > 0:
            self.x = self.x-1
        elif direction=="A" and self.y > 0:
            self.y = self.y - 1
        elif direction=="S" and self.x < board.size:
            self.x = self.x + 1
        elif direction=="D" and self.y < board.size:
            self.y = self.y+1

        board.update_board(self.x, self.y, "P")

    def is_finished(self, wumpus, gold):
        if self.x == wumpus.x and self.y == wumpus.y:
            print("Anda kalah 😭")
            return True
        elif self.x == gold.x and self.y == gold.y:
            print("Selamat, Anda menang 😄")
            return True
        return False

def movement():
    while True:
        move = input("masukkan gerakan: ").upper()
        if move in ["W", "A", "S", "D"]:
            break

    return move

def main():
    board_size = 10
    myBoard = Board(board_size)
    myPlayer = Player()
    wumpus = Wumpus(random.randint(0, board_size - 1), random.randint(0, board_size - 1))
    gold = Gold(random.randint(0, board_size - 1), random.randint(0, board_size - 1))

    myBoard.init_board(myPlayer, wumpus, gold)
   
    while True:
        myBoard.print_board()
        dir = movement()
        myPlayer.move(myBoard, dir, wumpus)
        
        if myPlayer.is_finished(wumpus, gold):
            myBoard.print_board()
            break


main()
    
