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
    b = []
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        # board.print_grid(game_board)
        if (not game_end):
            b = game_board
            connectFour = ConnectFour(game_board)
            # col = connectFour.minimax(4, True)
            print('\n')
            connectFour.print_grid()

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        random_column = random.randint(0, 6)
        board.select_column(random_column)
        time.sleep(2)
    print(b)
    print("Website won")


if __name__ == "__main__":
    main()
