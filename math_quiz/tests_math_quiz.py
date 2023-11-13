import unittest
from dsss_ex02 import create_random_integer, select_random_operator, perform_calculation


class TestMathGame(unittest.TestCase):

    def test_create_random_integer(self):
        # test if random numbers generated are within the specified range
        min_value: int = 1
        max_value: int = 10

        # test a large number of random values
        for _ in range(100):
            random_int: int = create_random_integer(min_value, max_value)
            self.assertTrue(min_value <= random_int <= max_value)

    def test_select_random_operator(self):
        # call the function multiple times and compare the returned values to a list of valid operators
        valid_operators: list = ['+', '-', '*']
        for _ in range(100):
            random_operator: str = select_random_operator()
            self.assertTrue(random_operator in valid_operators)

    def test_perform_calculations(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '-', '4 - 6', -2),
            (1, 8, '*', '1 * 8', 8),
            (0, 5, '*', '0 * 5', 0)
        ]

        for number_1, number_2, operator, expected_problem, expected_answer in test_cases:
            function_problem, function_answer = perform_calculation(number_1, number_2, operator)
            self.assertTrue(function_problem == expected_problem and function_answer == expected_answer)


if __name__ == "__main__":
    unittest.main()
