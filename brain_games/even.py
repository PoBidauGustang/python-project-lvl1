"""Game even."""
from random import randint
import prompt
from brain_games.cli import welcome_user


def game_even():
    """Answer 'yes' if number even otherwise answer 'no'"""
    print('\nWelcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".\n')
    name = welcome_user()
    for i in range (3):
        x = randint(0, 100)
        if x % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {0}'.format(str(x)))
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
