"""Game engine."""
from random import choice, randint

import prompt

NUMBER_OF_ROUNDS = 3


def run(game):
    """Run game.

    Args:
        game: Name of the game.
    """
    name = greetings(game.DISCRIPTION)
    count_of_rounds = 0
    while count_of_rounds < NUMBER_OF_ROUNDS:
        question, correct_answer = game.make_question()
        print(question)
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer".format(answer),
                ";(. Correct answer was '{0}'.".format(correct_answer),
                "\nLet's try again, {0}!".format(name),
            )
            return
        count_of_rounds += 1
    print('Congratulations, {0}!'.format(name))


def generate_operator():
    """Return random operator.

    Returns:
        Operator.
    """
    return choice(['+', '-', '*'])


def generate_number():
    """Return random number from range.

    Returns:
        End of loop.
    """
    return randint(1, 100)


def greetings(rules):
    """Brain games greeting. Get an user name and promt user.

    Args:
        rules: Discription of game`s rules.

    Returns:
        Name.
    """
    print('Welcome to the Brain Games!\n{0}'.format(rules))
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
