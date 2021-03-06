"""Game even."""
from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    random_int = randint(1, 100)
    question = ('{0}'.format(random_int))
    expected_answer = 'yes' if is_even(random_int) else 'no'
    return (question, expected_answer)


def is_even(integer):
    """Check if number is even or not.

    Args:
        integer: Game`s object.

    Returns:
        Bool.
    """
    return integer % 2 == 0
