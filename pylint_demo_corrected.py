
""" Contains the class Calculator """


class Calculator:
    """ Defining the methods of Calculator in here """
    answer = 0

    def addition(self, num1, num2):
        """ Adds the given two numbers and returns the answer """
        self.answer = num1 + num2
        return self.answer

    def subtraction(self, num1, num2):
        """ Subtracts the given two numbers and returns the answer """
        self.answer = num1 - num2
        return self.answer

    def multiplication(self, num1, num2):
        """ Multiplies the given two numbers and returns the answer """
        self.answer = num1 * num2
        return self.answer

    def division(self, num1, num2):
        """ Divides the given two numbers and returns the answer """
        self.answer = num1 / num2
        return self.answer
