"""Find the palindromes in a given txt file."""
from load_dictionary import load


def is_palindrome(word: str) -> bool:
    """Given a string checks if its a palindrome."""
    left_idx, right_idx = 0, len(word) - 1

    while left_idx < right_idx:
        if word[left_idx] != word[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def main():
    """Run the entrypoint of the program."""
    path_file = "/Users/cristofernava/Desktop/impratical_projects/chapter2/2of12.txt"

    words = load(path_file)
    palindromes = []
    for word in words:
        if len(word) > 1 and is_palindrome(word):
            palindromes.append(word)

    for palindrome in palindromes:
        print(palindrome)


if __name__ == "__main__":
    main()
