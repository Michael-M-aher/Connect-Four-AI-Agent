EMPTY = 0
RED = 1
BLUE = 2


class Board:
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]
        self.empty_spaces = 42

    def print_grid(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == EMPTY:
                    print("*", end=" ")
                elif self.board[i][j] == RED:
                    print("R", end=" ")
                elif self.board[i][j] == BLUE:
                    print("B", end=" ")
            print("\n")

    def get_game_grid(self):
        return self.board

    # place a piece in the column and return the row and column of the piece
    def place_piece(self, column, player):
        for i in range(len(self.board)-1, -1, -1):
            row = self.board[i]
            if row[column] == EMPTY:
                row[column] = player
                self.empty_spaces -= 1
                return i, column
        return -1, -1

    # check if the board is full
    def check_draw(self):
        return (self.empty_spaces == 0)

    # check if there are 4 in a row in any direction
    def check_win(self, row, column, player):
        return self._check_horizontal_win(row, column, player) or self._check_vertical_win(row, column, player) or self._check_positive_diagonal_win(row, column, player) or self._check_negative_diagonal_win(row, column, player)

    # go right and check if there are 4 right in a row
    def _check_horizontal_win(self, row, column, player):
        for i in range(column, column - 4, -1):
            if (i > 3 or i < 0):
                continue
            r = self.board[row]
            if (r[i] == player and r[i+1] == player and r[i+2] == player and r[i+3] == player):
                return True
        return False

    # go down and check if there are 4 up in a row
    def _check_vertical_win(self, row, column, player):
        if (row < 3 and self.board[row+1][column] == player and self.board[row+2][column] == player and self.board[row+3][column] == player):
            return True
        return False

    # go left and down and check if there are 4 right up in a row
    def _check_positive_diagonal_win(self, row, column, player):
        for i in range(0,  4, 1):
            if (column-i > 3 or column - i < 0 or row+i < 3 or row+i > 5):
                continue
            if (self.board[row+i][column-i] == player and self.board[row+i-1][column-i+1] == player and self.board[row+i-2][column-i+2] == player and self.board[row+i-3][column-i+3] == player):
                return True
        return False

    # go left and up and check if there are 4 right down in a row
    def _check_negative_diagonal_win(self, row, column, player):
        for i in range(0,  4, 1):
            if (column-i > 3 or column - i < 0 or row-i > 2 or row-i < 0):
                continue
            if (self.board[row-i][column-i] == player and self.board[row-i+1][column-i+1] == player and self.board[row-i+2][column-i+2] == player and self.board[row-i+3][column-i+3] == player):
                return True
            return False
