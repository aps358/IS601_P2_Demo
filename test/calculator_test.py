"""Importing Calculator Class from calculator > calculator_simple.py for Testing"""
from calculator.calculator_simple import Calculator


def test_calculator_result():
    """ To check if calculator initial result is 0 """
    # Arrange
    calc_obj = Calculator()

    # Act
    result = calc_obj.get_result()

    # Assert
    assert result == 0


def test_calculator_add():
    """ To check if calculator addition result is correct """
    # Arrange
    num1 = 10
    num2 = 20
    calc_obj = Calculator()

    # Act
    calc_obj.addition(num1, num2)

    # Assert
    assert calc_obj.get_result() == 30


def test_calculator_subtract():
    """ To check if calculator subtraction result is correct """
    # Arrange
    num1 = 10
    num2 = 20
    calc_obj = Calculator()

    # Act
    calc_obj.subtraction(num1, num2)

    # Assert
    assert calc_obj.get_result() == -10


def test_calculator_multiply():
    """ To check if calculator multiplication result is correct """
    # Arrange
    num1 = 10
    num2 = 20
    calc_obj = Calculator()

    # Act
    calc_obj.multiplication(num1, num2)

    # Assert
    assert calc_obj.get_result() == 200


def test_calculator_divide():
    """ To check if calculator division result is correct"""
    # Arrange
    num1 = 20
    num2 = 10
    calc_obj = Calculator()

    # Act
    calc_obj.division(num1, num2)

    # Assert
    assert calc_obj.get_result() == 2
