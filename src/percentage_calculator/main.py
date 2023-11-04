import sys

def printHelp():
    print("Expected the following format: ")
    print("percentage_calculator <value> <increase>")

def main():
    arguments = sys.argv
    if len(arguments) < 3:
        printHelp()
        exit(1)

    value = float(arguments[1])
    increaseBy = float(arguments[2])

    from percentage_calculator.has_valid_input import has_valid_input
    if has_valid_input(value, increaseBy):
        from percentage_calculator.format_number import format_number
        from percentage_calculator.percentage_calculator import percentage_calculator
        result = format_number(percentage_calculator(value, increaseBy))
        print(result)
    else:
        printHelp()


if __name__ == '__main__':
    main()