def test_has_input():
    # Arrange
    value = None
    increaseBy = None

    # Act
    from lib.has_valid_input import has_valid_input
    good_input = has_valid_input(value, increaseBy)

    # Assert
    assert good_input == False
