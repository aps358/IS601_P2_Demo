""" Import Calculation Parent Class Constructor """

from calc_methods.calculation import Calculation

# This is multiplication method which inherits the calculation class constructor


class Multiplication(Calculation):
    """ Performs multiply between two values coming from Parent Class and gives the results """

    def getresult(self):
        """ Using self to reference the data contained in the object instance """
        return self.value_a * self.value_b
