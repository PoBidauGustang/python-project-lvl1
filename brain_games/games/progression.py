"""Game progression."""
from random import choice, randint

DESCRIPTION = 'What number is missing in the progression?'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    start_num, delta = randint(1, 10), randint(1, 10)
    progression = make_progression(start_num, delta)
    missing_number = choice(progression)
    formatted_progression = ' '.join([
        '..' if num == missing_number else str(num) for num in progression
    ])
    return (('{0}'.format(formatted_progression)), str(missing_number))


def make_progression(start_num, delta):
    """Generate arithemtic progression.

    Args:
        start_num: First number of progression.
        delta: Progression step

    Returns:
        Progression.
    """
    length = 10
    progression = list(range(start_num, (length * delta) + start_num, delta))
    return progression
