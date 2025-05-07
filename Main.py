import Game

if __name__ == "__main__":
    game = Game.Game()

    print("Welcome to Tic Tac Toe!")

    i = 0
    turns = 0
    while i <= 9 and turns < 100:
        i += game.place(i % 2, i // 3)
        print(game.__str__())
        print(i)
        print(turns)
        turns += 1
    