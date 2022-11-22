"""Generate funny names by randomly combining names from 2 separete lists."""
import random

def generate_name() -> str:
    """Generate a cool name with a first and a second last name."""
    first_names = ["pedro", "juan", "lalo"] # list of first names
    last_names = ["picapiedra", "caza gigantes", "landa"] # list of second names

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    full_name = f"{first_name} {last_name}"

    return full_name



def main():
    """Run main function. Entry point."""
    print("Welcome to cool names, let's generate some cool names!")

    while True:
        user_input = input("Press enter to generate a new cool name. Press 'q' to exit of the game: ")

        if user_input == "q":
            break

        name = generate_name()
        print(f"Your cool name is: {name}")
        print()


if __name__ == "__main__":
    main()
