
"""Importing Calculator Class from calculator > calculator_simple.py for Testing"""
from calculator.calculator_simple import Calculator
import pandas as pd

csv_data = pd.read_csv('data/data.csv')
num1 = csv_data['num_1'].values
num2 = csv_data['num_2'].values
add = [round(i, 3) for i in csv_data['add_nums'].values]
sub = [round(i, 3) for i in csv_data['sub_nums'].values]
multi = [round(i, 3) for i in csv_data['mult_nums'].values]
div = [round(i, 3) for i in csv_data['div_nums'].values]
length = len(add)


def test_calculator_add():
    """ To check if calculator addition result is correct """
    # Arrangedata.csv
    calc_obj = Calculator()

    # Act and Assert
    for i in range(length):
        assert calc_obj.addition(num1[i], num2[i]) == add[i]


def test_calculator_subtract():
    """ To check if calculator subtraction result is correct """
    # Arrange
    calc_obj = Calculator()

    # Act and Assert
    for i in range(length):
        assert calc_obj.subtraction(num1[i], num2[i]) == sub[i]


def test_calculator_multiply():
    """ To check if calculator multiplication result is correct """
    # Arrange
    calc_obj = Calculator()

    # Act and Assert
    for i in range(length):
        assert calc_obj.multiplication(num1[i], num2[i]) == multi[i]


def test_calculator_divide():
    """ To check if calculator division result is correct"""
    # Arrange
    calc_obj = Calculator()

    # Act and Assert
    for i in range(length):
        assert calc_obj.division(num1[i], num2[i]) == div[i]
