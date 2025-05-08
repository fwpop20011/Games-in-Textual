import TicTacToeGame

if __name__ == "__main__":
    game = TicTacToeGame.Game()

    print("Welcome to Tic Tac Toe!")
    game.print_board()
    i = 0
    turns = 0
    while i <= 9 and turns <= 100 and game.winner == 0:
        print()
        print(game.player_turn())
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            i += game.place(row, col)
            game.print_board()
        except ValueError:
            print("Invalid input")
        turns += 1
        print(f"turn {turns}, round {i}")

    if turns == 100 and game.winner is None:
        print("No winner")
        exit()

    if game.winner is not None:
        print("Game over")
        if game.winner == 1:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        exit()
