"""Game even."""
from random import randint

DISCRIPTION = 'Answer "yes" if number even otherwise answer "no".\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    random_int = randint(1, 100)
    question = ('{0}'.format(random_int))
    expected_answer = 'yes' if is_even(random_int) else 'no'
    return (question, expected_answer)


def is_even(random_int):
    """Check if number is even or not.

    Args:
        random_int: Game`s object.

    Returns:
        Bool.
    """
    return not bool if random_int % 2 else bool
