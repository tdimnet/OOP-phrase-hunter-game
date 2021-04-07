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

        while self.missed < self.max_number_of_attempts:
            self.active_phrase.display(self.guesses)

            self.get_guess()

            print("====")
            print(self.missed)
            print("====")
            print("====")
            print(self.guesses)
            print("====")

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)

    def welcome(self):
        print("")
        print("==============================")
        print("   Welcome to Phrase Hunter   ")
        print("==============================")

    def get_guess(self):
        letter = input("Guess a letter: ")

        if not self.active_phrase.check_letter(letter):
            self.missed += 1

            print("\nYou have {} out of {} lives remaining!".format(self.missed, self.max_number_of_attempts))

        self.guesses.append(letter)

    def game_over(self):
        pass
