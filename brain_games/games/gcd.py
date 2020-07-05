"""Game gcd."""
from brain_games.games import engine


def game_gcd():
    """Answer greatest common divisor of given numbers."""
    engine.greetings()
    print('Find the greatest common divisor of given numbers.', end='\n\n')
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        correct_answer = engine.gcd()
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
