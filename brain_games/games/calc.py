"""Game even."""
from random import choice, randint

from brain_games.games import engine


def game_calc():
    """Answer result of the expression."""
    engine.greetings()
    print('What is the result of the expression?', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        sequence = ['+', '-', '*']
        rand_int1 = randint(0, 100)
        rand_int2 = randint(0, 100)
        rand_operator = choice(sequence)
        if rand_operator == '+':
            correct_answer = str(rand_int1 + rand_int2)
        elif rand_operator == '-':
            correct_answer = str(rand_int1 - rand_int2)
        else:
            correct_answer = str(rand_int1 * rand_int2)
        print(
            'Question: {0}'.format(str(rand_int1)),
            '{0} {1}'.format(rand_operator, str(rand_int2)),
        )
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer".format(answer),
                ";(. Correct answer was '{0}'.".format(correct_answer),
                "\nLet's try again, {0}!".format(name),
            )
            return
    print('Congratulations, {0}!'.format(name))
