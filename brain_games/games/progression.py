"""Game even."""
from random import randint

from brain_games.games import engine


def game_progression():
    """Answer missing number."""
    engine.greetings()
    print('What number is missing in the progression?', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        progression = engine.progression()
        replaced_num = randint(0, 9)
        correct_answer = progression.pop(replaced_num)
        progression.insert(replaced_num, '..')
        print('Question: {0}'.format(' '.join(map(str, progression))))
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
