"""Game calculator."""
from operator import mul
from random import choice, randint

DISCRIPTION = 'What is the result of the expression?\n'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = generate_operator()
    question = ('{0} {1} {2}'.format(num1, operator, num2))
    expected_answer = str(find_correct_answer(num1, num2, operator))
    return (question, expected_answer)


def find_correct_answer(num1, num2, operator):
    """Find correct answer.

    Args:
        num1: First number of game`s question.
        num2: Second number of game`s question.
        operator: Operator of game`s question.

    Returns:
        Correct answer.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    return mul(num1, num2)


def generate_operator():
    """Return random operator.

    Returns:
        Operator.
    """
    return choice(['+', '-', '*'])
