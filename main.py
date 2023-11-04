import sys

from format_number import format_number
from has_valid_input import has_valid_input
from percentage_calculator import percentage_calculator


def printHelp():
    print("Expected the following format: ")
    print("percentage_calculator <value> <increase>")


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) < 3:
        printHelp()
        exit(1)

    value = int(arguments[1])
    increaseBy = int(arguments[2])

    if has_valid_input(value, increaseBy):
        result = format_number(percentage_calculator(value, increaseBy))
        print(result)
    else:
        printHelp()