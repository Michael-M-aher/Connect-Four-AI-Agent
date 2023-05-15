from board import Board

EMPTY = 0
RED = 1
BLUE = 2


class Game:
    def __init__(self):
        self.player1 = RED
        self.player2 = BLUE
        self.game_over = False
        self.board = Board()

    def player1Turn(self):
        column = int(input(
            f"Player 1, it's your turn ,enter the column number you want to drop your piece in(1-{self.board.getNumColumns()}): "))
        if (column < 1 or column > self.board.getNumColumns()):
            print(
                f"Invalid column number, please enter a number between 1 and {self.board.getNumColumns()}")
            self.player1Turn()
            return
        column = column - 1
        row, column = self.board.place_piece(column, self.player1)
        if row == -1 and column == -1:
            print("Column is full, please choose another column")
            self.player1Turn()
            return
        print(row, column)
        if (self.board.check_win(row, column, self.player1)):
            self.board.print_grid()
            print("Player 1 wins!")
            self.game_over = True
            return
        if self.board.check_draw():
            self.board.print_grid()
            print("Draw!")
            self.game_over = True
            return

    def player2Turn(self):
        column = int(input(
            f"Player 2, it's your turn ,enter the column number you want to drop your piece in(1-{self.board.getNumColumns()}): "))
        if (column < 1 or column > self.board.getNumColumns()):
            print(
                f"Invalid column number, please enter a number between 1 and {self.board.getNumColumns()}")
            self.player2Turn()
            return
        column = column - 1
        row, column = self.board.place_piece(column, self.player2)
        if row == -1 and column == -1:
            print("Column is full, please choose another column")
            self.player2Turn()
            return
        print(row, column)
        if (self.board.check_win(row, column, self.player2)):
            self.board.print_grid()
            print("Player 2 wins!")
            self.game_over = True
            return
        if self.board.check_draw():
            self.board.print_grid()
            print("Draw!")
            self.game_over = True
            return
