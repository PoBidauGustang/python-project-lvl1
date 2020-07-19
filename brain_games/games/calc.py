"""Game calculator."""
from random import choice

from brain_games import engine

DISCRIPTION = 'What is the result of the expression?\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    num1 = engine.randint(1, 100)
    num2 = engine.randint(1, 100)
    operation = generate_operator()
    question = ('{0} {1} {2}'.format(num1, operation, num2))
    expected_answer = str(correct_answer(num1, num2, operation))
    return (question, expected_answer)


def correct_answer(num1, num2, operation):
    """Correct answer.

    Args:
        num1: First number of game`s question.
        num2: Second number of game`s question.
        operation: Operator number of game`s question.

    Returns:
        Correct answer.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    return num1 * num2


def generate_operator():
    """Return random operator.

    Returns:
        Operator.
    """
    return choice(['+', '-', '*'])
