class Player(object):
    # Kelas Player ini boleh ditambahkan atribut/ method lain, tapi jangan menghapus/ mengubah kode yang sudah ada
    # You can add other attributes and/or methods to this Player class, but don't delete or change the existing code.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.num_movement = 0
        self.percept = {
            "stench" : False,
            "breeze": False,
        }
        # TAMBAHAN ATRIBUT: prev_coor to know apakah Player berhasil bergerak / menghantam tembok
        self.prev_coor = (self.x, self.y)
        # TAMBAHAN ATRIBUT: safe_tile_or_not {id_tile: True/False}
        self.safe_or_not = {}
        # TAMBAHAN ATRIBUT: hasil percept per tile {id_tile: [stench, breeze]}
        self.percept_space = {}
        # TAMBAHAN ATRIBUT: tile yang ingin di-percept
        self.tile_need_to_be_checked = [(self.x, self.y)]

    def move(self, board, direction):
        board.update_board(self.x, self.y, board.board_static[self.x][self.y])

        if direction=="W" and self.x > 0:
            self.x = self.x-1
        elif direction=="A" and self.y > 0:
            self.y = self.y - 1
        elif direction=="S" and self.x < board.size-1:
            self.x = self.x + 1
        elif direction=="D" and self.y < board.size-1:
            self.y = self.y+1


        board.update_board(self.x, self.y, "P")
        self.percept["stench"] = board.board_static[self.x][self.y] == "~" or board.board_static[self.x][self.y] == "≌"
        self.percept["breeze"] = board.board_static[self.x][self.y] == "=" or board.board_static[self.x][self.y] == "≌"

    def is_finished(self, listWumpus, listPit, gold):
        for wumpus in listWumpus:
            if self.x == wumpus.x and self.y == wumpus.y:
                print("======================\nYou are eaten by Wumpus. You lose 😭")
                return True
        for pit in listPit:
            if self.x == pit.x and self.y == pit.y:
                print("======================\nYou fall into the pit. You lose 😭")
                return True
        if self.x == gold.x and self.y == gold.y:
            print("======================\nCongratulations, you win 😄")
            return True
        return False