class Calculator:

    answer = 0

    def addition(self, num1, num2):
        self.answer = num1 + num2
        return self.answer

    def subtraction(self, num1, num2):
        self.answer = num1 - num2
        return self.answer

    def multiplication(self, num1, num2):
        self.answer = num1 * num2
        return self.answer

    def division(self, num1, num2):
        self.answer = num1 / num2
        return self.answer
