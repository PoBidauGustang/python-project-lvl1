"""Game prime."""
from brain_games.games import engine

DISCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    num = engine.generate_number()
    question = ('Question: {0}'.format(num))
    expected_answer = correct_answer(num)
    return (question, expected_answer)


def correct_answer(num):
    """Correct answer.

    Args:
        num: Number of game`s question.

    Returns:
        Correct answer.
    """
    if num == 1:
        return 'no'
    for integer in range(2, (num // 2) + 1):
        if num % integer == 0:
            return 'no'
    return 'yes'
