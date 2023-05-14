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
