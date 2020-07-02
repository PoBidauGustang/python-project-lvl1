"""Game even."""
from random import choice, randint, randrange

from brain_games.games import engine

output0 = 'Question: {0}'
output1 = 'Your answer: '
output2 = 'Correct!'
output3 = "'{0}' is wrong answer"
output4 = ";(. Correct answer was '{0}'."
output5 = "\nLet's try again, {0}!"
output6 = 'Congratulations, {0}!'
new_string = '\n'


def game_even():
    """Answer 'yes' if number even otherwise answer 'no'."""
    engine.greetings()
    print('Answer "yes" if number even otherwise answer "no".', new_string)
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        random_int = randint(0, 100)
        if random_int % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(output0.format(str(random_int)))
        answer = input(output1)
        if answer == str(correct_answer):
            print(output2)
        else:
            print(
                output3.format(answer),
                output4.format(correct_answer),
                output5.format(name),
            )
            return
    print(output6.format(name))


def game_calc():
    """Answer result of the expression."""
    engine.greetings()
    print('What is the result of the expression?', new_string)
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
            output0.format(str(rand_int1)),
            '{0} {1}'.format(rand_operator, str(rand_int2)),
        )
        answer = input(output1)
        if answer == str(correct_answer):
            print(output2)
        else:
            print(
                output3.format(answer),
                output4.format(correct_answer),
                output5.format(name),
            )
            return
    print(output6.format(name))


def game_gcd():
    """Answer greatest common divisor of given numbers."""
    engine.greetings()
    print('Find the greatest common divisor of given numbers.', new_string)
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        rand_int1 = randint(1, 100)
        rand_int2 = randint(1, 100)
        correct_answer = engine.gcd(rand_int1, rand_int2)
        print('Question: {0} {1}'.format(rand_int1, rand_int2))
        answer = input(output1)
        if answer == str(correct_answer):
            print(output2)
        else:
            print(
                output3.format(answer),
                output4.format(correct_answer),
                output5.format(name),
            )
            return
    print(output6.format(name))


def game_progression():
    """Answer missing number."""
    engine.greetings()
    print('What number is missing in the progression?', new_string)
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        progression = engine.progression()
        replaced_num = randint(0, 9)
        correct_answer = progression.pop(replaced_num)
        progression.insert(replaced_num, '..')
        print(output0.format(' '.join(map(str, progression))))
        answer = input(output1)
        if answer == str(correct_answer):
            print(output2)
        else:
            print(
                output3.format(answer),
                output4.format(correct_answer),
                output5.format(name),
            )
            return
    print(output6.format(name))


def game_prime():
    """Answer missing number."""
    engine.greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".', new_string)
    name = engine.name_request()
    for iteration in (0, 1, 2):
        iteration += 1
        rand_num = randrange(1, 100, 2)
        correct_answer = engine.prime(rand_num)
        print(output0.format(rand_num))
        answer = input(output1)
        if answer == str(correct_answer):
            print(output2)
        else:
            print(
                output3.format(answer),
                output4.format(correct_answer),
                output5.format(name),
            )
            return
    print(output6.format(name))
