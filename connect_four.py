from board import RED, BLUE, EMPTY
import math


middleFactor = 128
winningFactor = 30
winScore = 200
loseScore = -200


class ConnectFour:
    def __init__(self, board, maxDepth=5, numRows=6, numColumns=7) -> None:
        self.numRows = numRows
        self.numColumns = numColumns
        # self.board = [[EMPTY for i in range(numColumns)]
        #               for j in range(numRows)]
        self.board = board
        self.maxDepth = maxDepth
        self.empty_spaces = (numRows*numColumns)

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

    def getNumColumns(self):
        return self.numColumns

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
        for i in range(self.numColumns):
            if self.board[0][i] == EMPTY:
                return False
        return True

    # check if there are 4 in a row in any direction
    def check_win(self, row, column, player):
        return self._check_horizontal_win(row, column, player) or self._check_vertical_win(row, column, player) or self._check_positive_diagonal_win(row, column, player) or self._check_negative_diagonal_win(row, column, player)

    # go right and check if there are 4 right in a row
    def _check_horizontal_win(self, row, column, player):
        for i in range(column, column - 4, -1):
            if (i > (self.numColumns-4) or i < 0):
                continue
            r = self.board[row]
            if (r[i] == player and r[i+1] == player and r[i+2] == player and r[i+3] == player):
                return True
        return False

    # go down and check if there are 4 up in a row
    def _check_vertical_win(self, row, column, player):
        if (row < (self.numRows-3) and self.board[row+1][column] == player and self.board[row+2][column] == player and self.board[row+3][column] == player):
            return True
        return False

    # go left and down and check if there are 4 right up in a row
    def _check_positive_diagonal_win(self, row, column, player):
        for i in range(0,  4, 1):
            if (column-i > (self.numColumns-4) or column - i < 0 or row+i < 3 or row+i > (self.numRows-1)):
                continue
            if (self.board[row+i][column-i] == player and self.board[row+i-1][column-i+1] == player and self.board[row+i-2][column-i+2] == player and self.board[row+i-3][column-i+3] == player):
                return True
        return False

    # go left and up and check if there are 4 right down in a row
    def _check_negative_diagonal_win(self, row, column, player):
        for i in range(0,  4, 1):
            if (column-i > (self.numColumns-4) or column - i < 0 or row-i > (self.numRows-4) or row-i < 0):
                continue
            if (self.board[row-i][column-i] == player and self.board[row-i+1][column-i+1] == player and self.board[row-i+2][column-i+2] == player and self.board[row-i+3][column-i+3] == player):
                return True
            return False

    def find_valid_columns(self):
        valid_columns = []
        for i in range(0, self.numColumns):
            if self.board[0][i] == EMPTY:
                valid_columns.append(i)
        return valid_columns

    def bestColumn(self):
        bestColumn = -1
        maxScore = -math.inf
        valid = self.find_valid_columns()
        for col in valid:
            (row, column) = self.place_piece(col, RED)
            # call minimax to get the score from the simulation ahead
            score = self.minimax([row, column], -math.inf,
                                 math.inf, math.inf, False)
            self.board[row][column] = EMPTY
            if score > maxScore:
                bestColumn = col
                maxScore = score
        return bestColumn

    def minimax(self, lastPlay, depth, alpha, beta, maximizing):
        valid = self.find_valid_columns()
        isTerminal = self.is_terminal_node(lastPlay[0], lastPlay[1])
        if (depth == 0):
            return -10
        if (isTerminal != None):
            return isTerminal

        if (maximizing):
            maxScore = -math.inf
            for col in valid:
                (row, column) = self.place_piece(col, RED)
                # call minimax to get the score from the simulation ahead
                score = self.minimax(
                    [row, column], depth-1, alpha, beta, False)
                self.board[row][column] = EMPTY
                maxScore = max(maxScore, score)
                alpha = max(alpha, maxScore)
                if beta <= alpha:
                    break
        else:
            maxScore = math.inf
            for col in valid:
                (row, column) = self.place_piece(col, BLUE)
                # call minimax to get the score from the simulation ahead
                score = self.minimax([row, column], depth-1, alpha, beta, True)
                self.board[row][column] = EMPTY
                maxScore = min(maxScore, score)
                beta = min(beta, maxScore)
                if beta <= alpha:
                    break
        return maxScore


    # check if board contains a win, lose or draw and return ther score
    def is_terminal_node(self, row, col):
        if (self.check_draw()):
            return 0
        elif self.check_win(row, col, RED):
            return winScore
        elif self.check_win(row, col, BLUE):
            return loseScore
        return None

    # calculate the score according to number of pieces in the middle
    def getMiddleScore(self, color):
        score = 0
        for i in range(7):
            for j in range(5, -1, -1):
                # column empty from below
                if (self.board[j][i] == EMPTY):
                    break
                if (self.board[j][i] == color):
                    score += middleFactor / (abs(i - 3) + 1)
                else:
                    score -= middleFactor / (abs(i - 3) + 1)
        return score