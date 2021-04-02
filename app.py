# Import your Game class
from phrase_hunter.game import Game

# Create your Dunder Main statement.
def main():
    game = Game()

    game.start()

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
if __name__ == "__main__":
    main()
