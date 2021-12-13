""" This is the increment function"""
# first import the addition namespace
from calci.calculator.main import Calculator


class CalculatorHistory:
    """This is the Calculator class"""

    # this is the calculator static property
    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Some"""
        return CalculatorHistory.history[0]

    @staticmethod
    def clear_history():
        """Some"""
        CalculatorHistory.history.clear()
        return True

    @staticmethod
    def history_count():
        """Some"""
        return len(CalculatorHistory.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """Some"""
        CalculatorHistory.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Some"""
        return CalculatorHistory.history[-1]

    @staticmethod
    def add_number(value_a, value_b):
        """adds number to result"""
        calc = Calculator()
        CalculatorHistory.add_calculation_to_history(calc.add_number(value_a, value_b))
        return CalculatorHistory.get_result_of_last_calculation_added_to_history()

    @staticmethod
    # this is an example of a calling method
    def subtract_number(value_a, value_b):
        """subtract number from result"""
        calc = Calculator()
        CalculatorHistory.add_calculation_to_history(
            calc.subtract_number(value_a, value_b)
        )
        return CalculatorHistory.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply two numbers and store the result"""
        calc = Calculator()
        CalculatorHistory.add_calculation_to_history(
            calc.multiply_numbers(value_a, value_b)
        )
        return CalculatorHistory.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """multiply two numbers and store the result"""
        calc = Calculator()
        CalculatorHistory.add_calculation_to_history(
            calc.divide_numbers(value_a, value_b)
        )
        return CalculatorHistory.get_result_of_last_calculation_added_to_history()
