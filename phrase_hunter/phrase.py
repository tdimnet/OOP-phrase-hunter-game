class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
    
    def display(self, guesses):
        placeholder = list()

        for letter in self.phrase:
            if letter.isalpha():
                if letter.lower() in guesses:
                    placeholder.append(letter)
                else:
                    placeholder.append("_")
            else:
                placeholder.append(letter)

        placeholder_phrase = "".join(placeholder)
        
        print("\n{}\n".format(placeholder_phrase))

    def check_letter(self, letter):
        pass

    def check_complete(self):
        pass
