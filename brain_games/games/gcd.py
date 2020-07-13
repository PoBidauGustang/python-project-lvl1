"""Game gcd."""
from brain_games.games import engine

DISCRIPTION = 'Find the greatest common divisor of given numbers.\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    num1 = engine.generate_number()
    num2 = engine.generate_number()
    question = ('Question: {0} {1}'.format(num1, num2))
    expected_answer = correct_answer(num1, num2)
    return (question, expected_answer)


def correct_answer(num1, num2):
    """Correct answer.

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
