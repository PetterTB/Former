import random


class FormerBoard:
    EMPTY = "."

    NOV_11 = [[1, 2, 3, 3, 3, 2, 1],
              [3, 2, 4, 3, 2, 2, 4],
              [2, 1, 4, 1, 3, 1, 3],
              [4, 3, 3, 3, 2, 4, 3],
              [1, 3, 4, 2, 1, 4, 2],
              [2, 4, 2, 4, 4, 2, 3],
              [4, 3, 2, 4, 4, 1, 1],
              [4, 3, 2, 4, 2, 2, 4],
              [2, 4, 3, 3, 3, 3, 1]]

    TEST1 = [[1, 2, 1],
             [2, 2, 1],
             [2, 1, 1]]

    def __init__(self):
        self.width = 7
        self.height = 9

        self.board = [[FormerBoard.EMPTY] * self.width] * self.height
        self.sectors = {}

    def get_deep_copy(self):
        res = FormerBoard()
        res.board = [row[:] for row in self.board]
        res.height = self.height
        res.width = self.width
        return res

    def remove_sector(self, h, w):
        size_of_sector = self._recursive_remove(h, w, self.board[h][w])
        self._perform_fall()
        return size_of_sector

    def print_board(self):
        print("board is: ")
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line += str(self.board[i][j])
            print(line)

    def load_board_11_nov(self):
        """ Min beste: 17, landets beste 14, snitt 19.
        """
        self.load_board(FormerBoard.NOV_11)

    def load_board(self, board):
        self.board = [i[:] for i in board]
        self.height = len(board)
        self.width = len(board[0])

    def find_sectors(self):
        """
         OBSOBS: Endrer midlertidig self.board. Single thread only.
        """

        self.sectors = {}

        saved_board = [row[:] for row in self.board]

        for h in range(len(self.board)):
            for w in range(len(self.board[h])):
                size = self._recursive_remove(h, w, self.board[h][w])
                if size > 0:
                    self.sectors[(h, w)] = size

        self.board = saved_board
        return self.sectors

    def find_random_sector(self):
        if self.is_empty():
            return 0, 0

        h = random.randrange(self.height)
        w = random.randrange(self.width)

        if self.board[h][w] == FormerBoard.EMPTY:
            return self.find_random_sector()
        else:
            return h, w

    def _recursive_remove(self, h, w, symbol):
        if h < 0 or w < 0:
            return 0
        if h >= self.height or w >= self.width:
            return 0

        symbol_found = self.board[h][w]

        if symbol_found == FormerBoard.EMPTY:
            return 0
        if symbol_found == symbol:
            self.board[h][w] = FormerBoard.EMPTY
            return (1 + self._recursive_remove(h - 1, w, symbol) +
                    self._recursive_remove(h + 1, w, symbol) +
                    self._recursive_remove(h, w + 1, symbol) +
                    self._recursive_remove(h, w - 1, symbol))
        return 0

    def _perform_fall(self):
        shape_fell = True
        while shape_fell:
            shape_fell = False
            for h in range(len(self.board) - 1):
                for w in range(len(self.board[h])):
                    has_symbol = self.board[h][w] != FormerBoard.EMPTY
                    below_empty = self.board[h + 1][w] == FormerBoard.EMPTY
                    if has_symbol and below_empty:
                        shape_fell = True
                        self.board[h + 1][w] = self.board[h][w]
                        self.board[h][w] = FormerBoard.EMPTY

    def is_empty(self):
        for shape in self.board[-1]:
            if shape != FormerBoard.EMPTY:
                return False
        return True
