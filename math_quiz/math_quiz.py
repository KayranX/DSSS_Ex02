import random
from typing import Tuple


def create_random_integer(min_value: int, max_value: int) -> int:
    """
    Create a random integer in range [min_value, max_value].

    Args:
    :param min_value: Lower bound
    :param max_value: Upper bound
    :return: Random integer within bounds
    """
    return random.randint(min_value, max_value)


def select_random_operator() -> str:
    """
    Select a random arithmetic operator from the set [+, -, *].

    Args:
    :return: Random arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def perform_calculation(number_1: int or float, number_2: int or float, operator: str) -> Tuple[str, int]:
    """
    Perform the calculations with the given operator on both given numbers.

    Args:
    :param number_1: First number to be used in the calculation
    :param number_2: Second number to be used in the calculation
    :param operator: Operator to determine the performed arithmetics
    :return: Formula for the calculation and its result
    """

    # create the formula for the computation and store it in a string
    formula: str = f"{number_1} {operator} {number_2}"

    # perform the calculation and return the formula and the result
    if operator == '+':
        result: int = number_1 + number_2
    elif operator == '-':
        result: int = number_1 - number_2
    else:
        result: int = number_1 * number_2
    return formula, result


def start_math_quiz():
    """
    Start a math quiz that will ask the user for solutions to given formulas and calculates a score.

    :return: Function does not return any values
    """

    # score stores the achieved result and iterations determines the amount of questions asked
    score: int = 0
    iterations: int = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # loop over the number of iterations to ask questions
    for _ in range(iterations):

        # determine the values and operator for the questions randomly
        number_1: int = create_random_integer(1, 10)
        number_2: int = create_random_integer(1, 6)
        operator: str = select_random_operator()

        # create the formula that will be given to the user
        formula, result = perform_calculation(number_1, number_2, operator)
        print(f"\nQuestion: {formula}")

        # read the input from the user and determine its validity, new prompt if the input is invalid
        while True:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Please enter an integer!")

        # give the user feedback whether their answer is correct
        if user_answer == result:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{iterations}")


if __name__ == "__main__":
    start_math_quiz()
