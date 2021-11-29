""" import all the methods from calc_methods"""
from calc_methods.addition import Addition
from calc_methods.subtraction import Subtraction
from calc_methods.multiplication import Multiplication
from calc_methods.division import Division


class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Clear the history array """
        Calculator.history.clear()

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        Calculator.history.append(calculation)

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation_added():
        """ Gets last calculation from history array """
        return Calculator.history[-1]

    @staticmethod
    def get_calculation_count():
        """ Gets number of calculations from history array """
        return len(Calculator.history)

    @staticmethod
    def add_nums(value_a, value_b):
        """ Adds given two numbers and appends the result to history """
        addition = Addition.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def subtract_nums(value_a, value_b):
        """ Subtracts given two numbers and appends the result to history """
        subtraction = Subtraction.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def multiply_nums(value_a, value_b):
        """ Multiplies given two numbers and appends the result to history """
        multiplication = Multiplication.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_last_calculation_added()

    @staticmethod
    def divide_nums(value_a, value_b):
        """ Divides given two numbers and appends the result to history """
        division = Division.create(value_a, value_b).getresult()
        Calculator.add_calculation_to_history(division)
        return Calculator.get_last_calculation_added()
