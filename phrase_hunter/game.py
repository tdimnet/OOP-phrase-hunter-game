import random

from phrase_hunter.phrase import Phrase


class Game:
    max_number_of_attempts = 5

    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = ""
        self.guesses = []
        self.missed = 0

    def start(self):
        self.welcome()
        self.get_random_phrase()

        while self.game_over():
            self.active_phrase.display(self.guesses)
            self.get_guess()

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)

    def welcome(self):
        print("")
        print("==============================")
        print("   Welcome to Phrase Hunter   ")
        print("==============================")

    def get_guess(self):
        is_guessing = True

        letter = ""

        while is_guessing:
            letter = input("Guess a letter: ")

            if len(letter) > 1 or not letter.isalpha():
                print("Wrong format")
            else:
                is_guessing = False

        if not self.active_phrase.check_letter(letter):
            self.missed += 1

            print("\nYou have {} out of {} tries!".format(self.missed, self.max_number_of_attempts))

        self.guesses.append(letter.lower())

    def game_over(self):
        if not self.missed < self.max_number_of_attempts:
            print("Bummer, you losse")
            return False

        if self.active_phrase.check_complete(self.guesses):
            print("Congrats, you won the game")
            return False

        return True
