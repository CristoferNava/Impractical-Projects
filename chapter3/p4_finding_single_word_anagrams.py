"""Use Python and a dictionary file to find all the single-word anagrams for
a given English word or a single name."""
import sys
import time


def read_file(file_path: str) -> list[str]:
    """Reads a file and return a list containin all the words in this file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = []
            for word in file:  # each line in the file is a word
                words.append(word.strip())
            return words

    except IOError as error:
        print(f"{error}. An error ocurred while trying to open the file.")

    sys.exit(1)


def is_anagram(word1: str, word2: str) -> bool:
    """Given two words of the same length check if the first word is an anagram
    of the second."""
    letters_frecuency = {}
    for letter in word1:
        if letter not in letters_frecuency:
            letters_frecuency[letter] = 0
        letters_frecuency[letter] += 1

    for letter in word2:
        if letter not in letters_frecuency or letters_frecuency[letter] == 0:
            return False
        letters_frecuency[letter] -= 1

    return True


def main():
    """Executes the program."""
    start = time.time()
    file_path = "/Users/cristofernava/Desktop/impratical_projects/chapter3/2of4brif.txt"
    words = read_file(file_path)

    input_word = "friend"
    anagrams = []
    for word in words:
        if len(word) == len(input_word):
            if is_anagram(word, input_word):
                anagrams.append(word)

    print(anagrams)
    end = time.time()
    print(f"Time: {end - start}")


if __name__ == "__main__":
    main()
