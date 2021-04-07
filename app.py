from phrase_hunter.game import Game

PHRASES = [
    # "May the Force be with you.",
    # "Elementary, my dear Watson.",
    # "My mama always said life was like a box of chocolates.",
    "My precious.",
    # "Bond. James Bond."
]


def main():
    game = Game(PHRASES)
    game.start()


if __name__ == "__main__":
    main()
