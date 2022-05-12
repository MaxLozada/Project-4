""" This is the Calculator Class"""


class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1):
        """ This is the add method"""
        self.result = self.result + value_1
        return self.result

    def subtract(self, value_1):
        """ This is the subtract method"""
        self.result = self.result - value_1
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result

    def division(self):
        """ Method for Division"""
        list_of_values = self.values[0]
        quotient_of_value = list_of_values[0]
        for value in list_of_values[1:]:
            try:
                quotient_of_value = quotient_of_value / float(value)
                return quotient_of_value
            except ZeroDivisionError as e:
                print(e)
                return "No Zero allowed in the Denominator!"
