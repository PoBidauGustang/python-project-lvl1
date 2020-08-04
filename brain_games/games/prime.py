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


def is_prime(integer):
    """Check if number is prime or not.

    Args:
        integer: Number of game`s question.

    Returns:
        Bool.
    """
    if integer <= 1:
        return False
    for num in range(2, int(sqrt(integer)) + 1):
        if integer % num == 0:
            return False
    return True
