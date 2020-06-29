"""Game even."""
from random import choice, randint

from brain_games.games import engine


def game_even():
    """Answer 'yes' if number even otherwise answer 'no'."""
    engine.greetings()
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        random_int = randint(0, 100)
        if random_int % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {0}'.format(str(random_int)))
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
    print('Congratulations, {0}!'.format(name))


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
        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'{0}' is wrong answer".format(answer),
                ";(. Correct answer was '{0}'.".format(correct_answer),
                "\nLet's try again, {0}!".format(name),
            )
            return
    print('Congratulations, {0}!'.format(name))


def game_gcd():
    """Answer greatest common divisor of given numbers."""
    engine.greetings()
    print('Find the greatest common divisor of given numbers.', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        rand_int1 = randint(1, 100)
        rand_int2 = randint(1, 100)
        correct_answer = engine.gcd(rand_int1, rand_int2)
        print('Question: {0} {1}'.format(rand_int1, rand_int2))
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
