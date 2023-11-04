import numbers


def has_valid_input(value, increaseBy):
    return isinstance(value, numbers.Number) and isinstance(increaseBy, numbers.Number)
