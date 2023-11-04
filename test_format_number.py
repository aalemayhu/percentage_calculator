from format_number import format_number


def test_format_number():
    # Arrange
    input = 108.33333333333333

    # Act
    result = format_number(input)

    # Assert
    assert  result == 108.33