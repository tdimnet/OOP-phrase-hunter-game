import random

from phrase_hunter.phrase import Phrase

class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.active_phrase = ""
        self.guesses = []
        self.missed = 0

    def start(self):
        self.welcome()
        self.get_random_phrase()

        while self.missed < 3:
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
        letter = input("Guess a letter: ")
        self.guesses.append(letter)

    def game_over(self):
        pass
