import random

PHRASES = [
    # "May the Force be with you.",
    # "Elementary, my dear Watson.",
    # "My mama always said life was like a box of chocolates.",
    "My precious.",
    # "Bond. James Bond."
]


def build_placeholder(phrase, test_letter):
    placeholder = []

    for letter in phrase:
        if letter.isalpha():
            if letter.lower() in test_letter:
                placeholder.append(letter)
            else:
                placeholder.append("_")
        else:
            placeholder.append(letter)


    return "".join(placeholder)


def choose_random_phrase():
    return random.choice(PHRASES)


def main():
    is_playing = True
    number_of_attempts = 0

    phrase = choose_random_phrase()
    selected_letters = []

    while is_playing:
        placeholder = build_placeholder(phrase, selected_letters)

        print(placeholder)

        selected_letter = input("Guess a letter: ")

        selected_letters.append(selected_letter.lower())


if __name__ == "__main__":
    main()
