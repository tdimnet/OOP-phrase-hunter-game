import random

PHRASES = [
    "May the Force be with you.",
    "Elementary, my dear Watson.",
    "My mama always said life was like a box of chocolates.",
    "My precious.",
    "Bond. James Bond."
]


def display_phrase(phrase, test_letter):
    print(list(phrase))
    print(test_letter)

    placeholder = []

    for letter in phrase:
        if letter.isalpha():
            if letter.lower() == test_letter.lower():
                placeholder.append(letter)
            else:
                placeholder.append("_")
        else:
            placeholder.append(letter)

    print("====")
    print("".join(placeholder))
    print("====")


def choose_random_phrase():
    return random.choice(PHRASES)


def main():
    phrase = choose_random_phrase()

    display_phrase(phrase, ["m"])

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
if __name__ == "__main__":
    main()
