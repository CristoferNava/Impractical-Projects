"""Load a text file as list.

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys

def load(file) -> list[str]:
    """Open a text file and return a list of lowercase strings."""
    try:
        with open(file, encoding="utf-8") as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print(f"Error opening. {error}")
    sys.exit(1) # Statement used to terminate the program.
                # The 1 indicates that the program expirenced an error and did not
                # not close successfully.
