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
