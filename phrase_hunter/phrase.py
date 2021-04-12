class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase

        self.filter_letters_in_phrase = list()
        for letter in list(self.phrase.lower()):
            if letter.isalpha() and not letter in self.filter_letters_in_phrase:
                self.filter_letters_in_phrase.append(letter)

    def display(self, guesses):
        placeholder = list()

        for letter in self.phrase:
            if letter.isalpha():
                if letter.lower() in guesses or letter.upper() in guesses:
                    placeholder.append(letter)
                else:
                    placeholder.append("_ ")
            else:
                placeholder.append(letter)

        placeholder_phrase = "".join(placeholder)
        
        print("\n{}\n".format(placeholder_phrase))

    def check_letter(self, guessed_letter):
        parse_to_lower = [letter.lower() for letter in self.phrase]
        
        return guessed_letter.lower() in parse_to_lower

    def check_complete(self, guesses_list):
        for letter in self.filter_letters_in_phrase:
            if not letter in guesses_list:
                return False
        
        return True