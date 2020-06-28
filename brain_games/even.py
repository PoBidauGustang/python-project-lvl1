"""Game even."""
from random import randint

from brain_games.cli import welcome_user


def game_even():
    """Answer 'yes' if number even otherwise answer 'no'."""
    print(
        '\nWelcome to the Brain Games!\nAnswer "yes" if ',
        'number even otherwise answer "no".',
        end='\n\n',
    )
    name = welcome_user()
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
                ";(. Correct answer was '{0}'.\n".format(correct_answer),
                "Let's try again, {0}!".format(name),
            )
            return
    print('Congratulations, {0}!'.format(name))
