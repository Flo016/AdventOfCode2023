from aoc_helper import file_helper
from aoc_helper.aoc_main import AdventOfCode

def load_days_and_print():
    """
    Loads the days from the aoc_days package and prints them
    Only the days that have at least one part that returns a result different from -1 are printed
    :return:
    """
    file_helper.create_files()
    aoc = AdventOfCode()
    aoc.load_days()
    aoc.print_days()


def main():
    """
    To get started with Advent of Code:
     - open the file for the day you want to complete in aoc_days (e.g. day01.py)
     - copy the input from the website into the dayXX_input.txt file (e.g. day01_input.txt)
     - Add a short name for the part you want to implement in the return parameter of the part_X method (Replace: <Name/Short Description of this part> with the name)
     - implement the puzzle in part_1 in the dayXX.py file.
       If there are more than one parts, add another part method with the same signature as part_1 (e.g. part_2, part_3 ...)

       To run the code -> run the main.py file (all Days and Parts that return a result different from -1 are printed)

       You can also add helper-methods for a day or a part in the dayXX.py file, as long as they are not called part_1, part_2, ...
    :return:
    """
    load_days_and_print()


if __name__ == '__main__':
    main()
