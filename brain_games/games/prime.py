"""Game prime."""
from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    random_int = randint(1, 100)
    question = ('{0}'.format(random_int))
    expected_answer = 'yes' if is_prime(random_int) else 'no'
    return (question, expected_answer)


def is_prime(random_int):
    """Check if number is prime or not.

    Args:
        random_int: Number of game`s question.

    Returns:
        Bool.
    """
    if random_int <= 1:
        return False
    for integer in range(2, int(sqrt(random_int)) + 1):
        if random_int % integer == 0:
            return False
    return True
