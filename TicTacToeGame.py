from wsgiref.util import request_uri

X = 1
O = -1

class Game:
    def __init__(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = X
        self.winner = 0
        self.game_over = False
        self.turns = 0

    def player_turn(self) -> str:
        if self.turn == X:
            return "X"
        else:
            return "0"

    def print_board(self) -> None:
        print(self.txt_board())

    def txt_board(self) -> str:
        txt = ""
        for row in self.board:
            txt = txt + "\n" + row.__str__()
        return txt

    def place(self, row, col) -> int:
        if self.board[row][col] == 0:
            self.board[row][col] = self.turn
            self.turn = O if self.turn == X else X
            self.winner = self.check_for_winner()
            self.turns += 1
            return 1
        else:
            print("That space is already taken!")
            return 0

    def check_for_winner(self) -> int:
        # check rows
        for i in range(3):
            row_sum = 0
            for j in range(3):
                row_sum += self.board[i][j]
            if row_sum == 3:
                self.game_over = True
                return X
            if row_sum == O*3:
                self.game_over = True
                return -O

        # check columns
        for j in range(3):
            col_sum = 0
            for i in range(3):
                col_sum += self.board[i][j]
            if col_sum == 3:
                self.game_over = True
                return X
            if col_sum == -3:
                self.game_over = True
                self.winner = O
                return O

        # check diagonal left to right
        diag_sum = 0
        for i in range(3):
            diag_sum += self.board[i][i]
        if diag_sum == 3:
            self.game_over = True
            self.winner = X
            return 100
        if diag_sum == -3:
            self.game_over = True
            self.winner = O
            return -100

        # check diagonal right to left
        diag_sum = 0
        for i in range(3):
            diag_sum += self.board[i][2 - i]
        if diag_sum == 3:
            self.game_over = True
            self.winner = X
            return 100
        if diag_sum == -3:
            self.game_over = True
            self.winner = O
            return -100

        return 0

    def reset(self) -> None:
        self.board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
        self.turn = X
        self.winner = 0
        self.game_over = False
        self.turns = 0