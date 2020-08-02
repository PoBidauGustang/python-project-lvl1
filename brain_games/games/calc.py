"""Game calculator."""
from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = generate_operator()
    question = ('{0} {1} {2}'.format(num1, operator, num2))
    expected_answer = str(calculate(num1, num2, operator))
    return (question, expected_answer)


def calculate(num1, num2, operator=mul):
    """Find correct answer.

    Args:
        num1: First number of game`s question.
        num2: Second number of game`s question.
        operator: Operator of game`s question.

    Returns:
        Correct answer.
    """
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    return mul(num1, num2)


def generate_operator():
    """Return random operator.

    Returns:
        Operator.
    """
    return choice(['+', '-', '*'])
