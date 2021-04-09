from phrase_hunter.game import Game

PHRASES = [
    "May the Force be with you",
    "Elementary, my dear Watson",
    "My mama always said life was like a box of chocolates",
    "My precious",
    "Bond. James Bond"
]


def main():
    is_playing = True

    while is_playing:
        is_asking = True

        game = Game(PHRASES)
        game.start()

        while is_asking:
            wants_to_play_again = input("Do you want to play again? [y]es/[n]o  ")

            if wants_to_play_again.lower() == "y":
                is_asking = False
            elif wants_to_play_again.lower() == "n":
                is_asking = False
                is_playing = False
                print("Ok, bye bye ;)")
            else:
                print("Wrong input")


if __name__ == "__main__":
    main()
