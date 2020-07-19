"""Game prime."""
from brain_games import engine

DISCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    random_int = engine.randint(1, 100)
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
    if random_int == 1:
        return False
    for integer in range(2, (random_int // 2) + 1):
        if random_int % integer == 0:
            return False
    return True
