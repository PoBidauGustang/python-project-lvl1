"""Game even."""
from random import randrange

from brain_games.games import engine


def game_prime():
    """Answer missing number."""
    engine.greetings()
    print(
        'Answer "yes" if given number is prime. ',
        'Otherwise answer "no".',
        end='\n\n',
    )
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        rand_num = randrange(1, 100, 2)
        correct_answer = engine.prime(rand_num)
        print('Question: {0}'.format(rand_num))
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
