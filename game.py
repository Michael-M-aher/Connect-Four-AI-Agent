from board import Board, RED
from connect_four import ConnectFour
import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# GAME LINK
# http://kevinshannon.com/connect4/

app = QApplication(sys.argv)


def main():
    main_screen = MainScreen()
    main_screen.show()
    sys.exit(app.exec_())


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.algorithm = 0
        self.difficulty = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Connect Four AI")
        self.resize(594, 327)

        self.widget = QWidget()
        layout = QGridLayout()
        layout.setSpacing(10)

        font = QFont()
        font.setPointSize(9)
        label_algorithmType = QLabel('AI Algorithm')
        label_algorithmType.setFont(font)
        algorithmType = QComboBox()
        algorithmType.setGeometry(QRect(240, 130, 221, 20))
        algorithmType.addItem('Select AI Algorithm')
        algorithmType.addItem('Minimax')
        algorithmType.addItem('Minimax Alpha Beta Pruning')
        algorithmType.currentIndexChanged.connect(self.AlgorithmChanged)
        layout.addWidget(label_algorithmType, 1, 0)
        layout.addWidget(algorithmType, 1, 1, 1, 2)

        label_difficulty = QLabel('Difficulty Level')
        label_difficulty.setFont(font)
        difficultyLevel = QComboBox()
        difficultyLevel.setGeometry(QRect(240, 130, 221, 20))
        difficultyLevel.addItem('Select Difficulty Level')
        difficultyLevel.addItem('Easy')
        difficultyLevel.addItem('Medium')
        difficultyLevel.addItem('Hard')
        difficultyLevel.currentIndexChanged.connect(self.DifficultyChanged)
        layout.addWidget(label_difficulty, 2, 0)
        layout.addWidget(difficultyLevel, 2, 1, 1, 2)

        button_start = QPushButton('Start')
        button_start.setGeometry(QRect(220, 200, 151, 61))
        button_start.clicked.connect(self.start)
        layout.addWidget(button_start, 4, 1)
        # layout.setRowMinimumHeight(2, 75)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def AlgorithmChanged(self, i):
        self.algorithm = i

    def DifficultyChanged(self, i):
        self.difficulty = i

    def start(self):
        if self.algorithm == 0 or self.difficulty == 0:
            self.statusbar.showMessage(
                "Please select AI Algorithm and Difficulty Level")
        else:
            depth = 0
            if self.difficulty == 1:
                depth = 2
            elif self.difficulty == 2:
                depth = 4
            elif self.difficulty == 3:
                depth = 5
            board = Board()

            time.sleep(5)
            game_end = False

            (game_board, game_end) = board.get_game_grid()

            while not game_end:
                (game_board, game_end) = board.get_game_grid()

                # FOR DEBUG PURPOSES
                board.print_grid(game_board)

                # YOUR CODE GOES HERE
                if (not game_end):
                    connectFour = ConnectFour(game_board, depth)
                    col = row = -1
                    if (self.algorithm == 1):
                        col, row = connectFour.bestColumnMinimax()
                    else:
                        col, row = connectFour.bestColumnMinimaxAlphaBeta()
                    board.select_column(col + 1)
                    connectFour.place_piece(col, RED)
                    if (connectFour.check_win(row, col, RED)):
                        self.statusbar.showMessage("AI won")
                        print("AI won")
                        return
                time.sleep(2)

            self.statusbar.showMessage("Website won")
            print("Website won")


if __name__ == "__main__":
    main()
