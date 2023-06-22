from game.game import Game

if __name__ == '__main__':

    new_game = Game()
    with open('moves.txt') as f:
        game_start = f.readline()
        if (game_start.strip() == "GAME-START"):
            move = f.readline()
            while move.strip() != "GAME-END":
                knight = move[0]
                direction = move[2]
                new_game.move(knight,direction)
                move = f.readline()

    new_game.print_board()