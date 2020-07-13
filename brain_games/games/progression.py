"""Game progression."""
from random import randint

DISCRIPTION = 'What number is missing in the progression?\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    expected_answer, prepared_question = correct_answer()
    question = prepared_question
    return (question, expected_answer)


def correct_answer():
    """Correct answer.

    Returns:
        Correct answer.
    """
    num = randint(1, 10)
    progress = list(range(num, (10 * num) + 1, num))
    replaced_num = randint(0, 9)
    missing_number = progress.pop(replaced_num)
    progress.insert(replaced_num, '..')
    question = ('Question: {0}'.format(' '.join(map(str, progress))))
    return (str(missing_number), question)
