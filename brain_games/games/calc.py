"""Game calculator."""
from brain_games.games import engine

DISCRIPTION = 'What is the result of the expression?\n'


def make_question():
    """Question.

    Returns:
        Question, expected player`s answer.
    """
    num1 = engine.generate_number()
    num2 = engine.generate_number()
    operation = engine.generate_operator()
    question = ('Question: {0} {1} {2}'.format(num1, operation, num2))
    expected_answer = correct_answer(num1, num2, operation)
    return (question, expected_answer)


def correct_answer(num1, num2, operation):
    """Correct answer.

    Args:
        num1: First number of game`s question.
        num2: Second number of game`s question.
        operation: Operator number of game`s question.

    Returns:
        Correct answer.
    """
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    return str(num1 * num2)
