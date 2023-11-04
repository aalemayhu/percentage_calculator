def percentage_calculator(value, increaseBy):
    return (value / increaseBy) + value

def test_returns_correct_value():
    # Arrange
    increaseBy = 10
    value = 100

    # Act
    newValue = percentage_calculator(value, increaseBy)

    # Assert
    assert newValue == 110