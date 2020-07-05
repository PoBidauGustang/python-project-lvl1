"""Game even."""
from brain_games.games import engine


def game_even():
    """Answer 'yes' if number even otherwise answer 'no'."""
    engine.greetings()
    print('Answer "yes" if number even otherwise answer "no".', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        correct_answer = engine.even()
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
