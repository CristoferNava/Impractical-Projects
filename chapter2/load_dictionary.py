"""Load a text file as a list.

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys 

def load(file: str) -> list[str]:
    """Open a text file and return a list of lowercase strings."""
    try:
        with open(file, "r") as in_file:
            word_list = [word.strip().lower() for word in in_file]
            return word_list 
    except IOError as error:
        print(f"{error}\nError opening {file}. Terminating program.")
    
    sys.exit(1) # Terminates the program.