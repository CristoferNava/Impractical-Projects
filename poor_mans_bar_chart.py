"""
Given a string print the bar chart of frecuency.
"""

def print_chart(text: str) -> None:
    """Given a text print a chart of the frecuency of each letter."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chars_frecuency = {}
    for char in alphabet:
        chars_frecuency[char] = 0

    for char in text:
        char = char.lower()
        if char in alphabet:
            chars_frecuency[char] += 1

    # build the chart
    for char, frecuency in chars_frecuency.items():
        print(f"{char}: ", end="")
        for _ in range(frecuency):
            print("* ", end="")
        print()


def main():
    """Run the main program."""
    print("Welcome the 'Letters Frecuency!'")

    while True:
        print("Enter a text to build the chart of letters frecuency.")
        print("Press '-' and enter to exit.")
        user_input = input(">>> ")

        if user_input == "-":
            break

        print_chart(user_input)
        print()


if __name__ == "__main__":
    main()
