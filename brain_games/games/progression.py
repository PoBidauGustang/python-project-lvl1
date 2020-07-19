"""Game progression."""
from brain_games.engine import randint

DISCRIPTION = 'What number is missing in the progression?\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    progress = make_progression()
    replaced_num = randint(0, 9)
    missing_number = progress.pop(replaced_num)
    progress.insert(replaced_num, '..')
    question = ('{0}'.format(' '.join(map(str, progress))))
    return (question, str(missing_number))


def make_progression():
    """Generate arithemtic progression.

    Returns:
        Progression.
    """
    num = randint(1, 10)
    progress = list(range(num, (10 * num) + 1, num))
    return progress
