import sys

from percentage_calculator import percentage_calculator

if __name__ == '__main__':
    arguments = sys.argv
    value = int(arguments[1])
    increaseBy = int(arguments[2])

    print(percentage_calculator(value, increaseBy))