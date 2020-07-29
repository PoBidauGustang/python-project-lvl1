"""Game gcd."""
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = ('{0} {1}'.format(num1, num2))
    expected_answer = find_gcd(num1, num2)
    return (question, expected_answer)


def find_gcd(num1, num2):
    """Find correct answer.

    Args:
        num1: First number of game`s question.
        num2: Second number of game`s question.

    Returns:
        Correct answer.
    """
    while num2 != 0:
        var_help = num2
        num2 = num1 % num2
        num1 = var_help
    return str(num1)
