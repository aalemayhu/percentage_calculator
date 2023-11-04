
def test_returns_correct_value():
    # Arrange
    increaseBy = 12
    value = 100

    # Act
    from lib.percentage_calculator import percentage_calculator
    newValue = percentage_calculator(value, increaseBy)

    # Assert
    assert newValue == 112.0