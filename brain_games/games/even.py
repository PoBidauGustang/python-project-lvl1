"""Game even functions."""
from brain_games.games import engine

DISCRIPTION = 'Answer "yes" if number even otherwise answer "no".\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    random_int = engine.generate_number()
    question = ('Question: {0}'.format(random_int))
    expected_answer = correct_answer(random_int)
    return (question, expected_answer)


def correct_answer(random_int):
    """Correct answer.

    Args:
        random_int: Game`s object.

    Returns:
        Correct answer.
    """
    return 'no' if random_int % 2 else 'yes'
