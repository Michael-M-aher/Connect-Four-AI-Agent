from game import Game


def main():
    # print("Welcome to Connect 4!")
    # print("Player 1 is Red")
    # print("Player 2 is Blue")
    # print("Player 1 goes first")
    # print("To play, enter the column number you want to drop your piece in")
    # print("The first player to get 4 in a row wins!")
    # print("Good luck!")
    # print("\n")
    # print("Here is the board:")
    # print(board.get_game_grid())
    game = Game()
    while not game.game_over:
        game.board.print_grid()
        game.player1Turn()
        if game.game_over:
            break
        game.board.print_grid()
        game.player2Turn()
    print("Game Over!")


if __name__ == "__main__":
    main()
