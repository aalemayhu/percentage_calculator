from has_valid_input import has_valid_input

def test_has_input():
    # Arrange
    value = None
    increaseBy = None

    # Act
    good_input = has_valid_input(value, increaseBy)

    # Assert
    assert good_input == False
