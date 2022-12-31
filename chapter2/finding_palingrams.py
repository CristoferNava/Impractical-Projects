"""Giving a file find all the words that are palindromes and returns a list of them."""
from load_dictionary import load


def check_palindrome(string: str) -> bool:
    """Given a string returns True if it is a palindrome otherwise returns False."""
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    file = "/Users/cristofernava/Desktop/impratical_projects/chapter2/2of4brif.txt"
    words = load(file)
    palindromes = []

    for word in words:
        if check_palindrome(word):
            palindromes.append(word)

    print(palindromes)


if __name__ == "__main__":
    main()
