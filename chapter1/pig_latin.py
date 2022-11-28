"""Take an English word and prints its 'Pig Latin' form."""


def to_pig_latin(word: str) -> str:
    """Given a word return its Pig Lati form."""

    consonants = "bcdfghjklmnpqrstvwxyz"

    if word[0] in consonants:
        # If the word begins with a consonant, move that consonant to the end
        # and add "ay"
        new_word = list(word[1:])
        new_word.extend([word[0], "a", "y"])
    else:
        # If the word begins with a vowel we simply add way to the end of the word
        new_word = list(word)
        new_word.extend(["w", "a", "y"])

    return "".join(new_word)


def main():
    """Entry point of the main function."""
    print("Welcome to Pig Latin!")

    while True:
        print("Write a word to transform it to Pig Latin. Press 'q' to exit.")
        user_input = input(": ")

        if user_input == "q":
            print("Thaks for playing. Bye!")
            break

        pig_latin_word = to_pig_latin(user_input)
        print(f"The word '{user_input}' in Pig Latin Word is {pig_latin_word}")


if __name__ == "__main__":
    main()
