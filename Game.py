TicTacToe_board = [["0","0","0"],
         ["0","0","0"],
         ["0","0","0"]]

class Game:
    def __init__(self):
        self.board = TicTacToe_board
        self.turn = 'X'
        self.winner = None
        self.game_over = False
    def __str__(self):
        txt = ""
        for row in self.board:
            txt = txt + "\n" + row.__str__()
        return txt

    def place(self, row, col):
        if self.board[row][col] == "0":
            self.board[row][col] = self.turn
            self.turn = "O" if self.turn == "X" else "X"
            self.check_for_winner()
            return 1
        else:
            print("That space is already taken!")
            return 0

    def check_for_winner(self):
        for i in range(3):
            pass

