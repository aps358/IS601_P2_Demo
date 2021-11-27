""" Define the class Calculator """


class Calculator:
    """ Creating a Module Calculator """

    # result set to 0 for initialization
    result = 0

    def get_result(self):
        """ Defining the get_result function """
        return self.result

    def addition(self, value_a, value_b):
        """ Defining the addition function """
        self.result = (value_a + value_b)

        # returns the result
        return self.result

    def subtraction(self, value_a, value_b):
        """ Defining the subtraction function """
        self.result = (value_a - value_b)

        # returns the result
        return self.result

    def multiplication(self, value_a, value_b):
        """ Defining the multiplication function """
        self.result = (value_a * value_b)

        # returns the result
        return self.result

    def division(self, value_a, value_b):
        """ Defining the division function """
        self.result = (value_a / value_b)

        # returns the result
        return self.result
