"""Game progression."""
from random import randint

DISCRIPTION = 'What number is missing in the progression?\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    progression = make_progression()
    replaced_num = randint(0, 9)
    missing_number = progression.pop(replaced_num)
    progression.insert(replaced_num, '..')
    question = ('{0}'.format(' '.join(map(str, progression))))
    return (question, str(missing_number))


def make_progression():
    """Generate arithemtic progression.

    Returns:
        Progression.
    """
    num = randint(1, 10)
    progression = list(range(num, (10 * num) + 1, num))
    return progression
