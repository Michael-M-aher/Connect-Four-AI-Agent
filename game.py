from board import Board
from connect_four import ConnectFour
import time
import random

# GAME LINK
# http://kevinshannon.com/connect4/


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        if (not game_end):
            connectFour = ConnectFour(game_board)
            print('\n')
            connectFour.print_grid()
            col = connectFour.bestColumn()

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        time.sleep(2)
    print("Website won")


if __name__ == "__main__":
    main()
