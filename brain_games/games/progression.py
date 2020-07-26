"""Game progression."""
from random import randint

DISCRIPTION = 'What number is missing in the progression?\n'


def make_question_and_correct_answer():
    """Question.

    Returns:
        Question; expected player`s answer.
    """
    num1 = randint(1, 10)
    progression = make_progression(num1)
    replaced_num = randint(0, 9)
    missing_number = progression.pop(replaced_num)
    progression.insert(replaced_num, '..')
    question = ('{0}'.format(' '.join(map(str, progression))))
    return (question, str(missing_number))


def make_progression(num1):
    """Generate arithemtic progression.

    Args:
        num1: First number of progression.

    Returns:
        Progression.
    """
    num_elements = 10
    progression = list(range(num1, (num_elements * num1) + 1, num1))
    return progression
