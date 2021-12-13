from calci.history.main import CalculatorHistory


def test_get_result_of_first_calculation_added_to_history():
    """Testing history"""
    CalculatorHistory.clear_history()
    CalculatorHistory.add_number(10, 4)
    assert CalculatorHistory.get_result_of_first_calculation_added_to_history() == 14


def test_clear_history():
    """Some"""
    CalculatorHistory.clear_history()
    CalculatorHistory.add_number(10, 4)
    assert len(CalculatorHistory.history) == 1
    assert CalculatorHistory.clear_history()
    assert len(CalculatorHistory.history) == 0


def test_history_count():
    """Some"""
    CalculatorHistory.clear_history()
    CalculatorHistory.add_number(10, 4)
    assert len(CalculatorHistory.history) == 1
    assert CalculatorHistory.history_count() == 1


def test_add_calculation_to_history():
    """Some"""
    CalculatorHistory.clear_history()
    some_value = 9
    assert CalculatorHistory.add_calculation_to_history(some_value)
    assert (
        CalculatorHistory.get_result_of_last_calculation_added_to_history()
        == some_value
    )


def test_get_result_of_last_calculation_added_to_history():
    """Some"""
    CalculatorHistory.clear_history()
    CalculatorHistory.add_calculation_to_history(8)
    CalculatorHistory.add_calculation_to_history(9)
    assert CalculatorHistory.get_result_of_last_calculation_added_to_history() == 9


def test_add_number():
    """adds number to result"""
    CalculatorHistory.clear_history()
    num_1 = 9
    num_2 = 3
    result = 12
    CalculatorHistory.add_number(num_1, num_2)
    assert result == CalculatorHistory.get_result_of_last_calculation_added_to_history()

def test_subtract_number():
    """subtract number to result"""
    CalculatorHistory.clear_history()
    num_1 = 9
    num_2 = 3
    result = 6
    CalculatorHistory.subtract_number(num_1, num_2)
    assert result == CalculatorHistory.get_result_of_last_calculation_added_to_history()

def test_multiply_number():
    """multiply number to result"""
    CalculatorHistory.clear_history()
    num_1 = 9
    num_2 = 3
    result = 27
    CalculatorHistory.multiply_numbers(num_1, num_2)
    assert result == CalculatorHistory.get_result_of_last_calculation_added_to_history()


def test_divide_number():
    """divide number to result"""
    CalculatorHistory.clear_history()
    num_1 = 9
    num_2 = 3
    result = 3
    CalculatorHistory.divide_numbers(num_1, num_2)
    assert result == CalculatorHistory.get_result_of_last_calculation_added_to_history()
