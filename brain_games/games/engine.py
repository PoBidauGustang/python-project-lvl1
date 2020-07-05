"""Game engine."""
from random import choice, randint

import prompt


def greetings():
    """Brain games greeting."""
    print('Welcome to the Brain Games!')


def name_request():
    """Get an user name and promt user.

    Returns:
        Name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name


def gcd():
    """Give gcd of two integers.

    Returns:
        grand_cd.
    """
    rand_int1 = randint(1, 100)
    rand_int2 = randint(1, 100)
    print('Question: {0} {1}'.format(rand_int1, rand_int2))
    while rand_int2 != 0:
        var_help = rand_int2
        rand_int2 = rand_int1 % rand_int2
        rand_int1 = var_help
    return rand_int1


def progression():
    """Progression().

    Returns:
        missing number.
    """
    num = randint(1, 10)
    progress = list(range(num, (10 * num) + 1, num))
    replaced_num = randint(0, 9)
    missing_number = progress.pop(replaced_num)
    progress.insert(replaced_num, '..')
    print('Question: {0}'.format(' '.join(map(str, progress))))
    return missing_number


def prime(arg):
    """Prime().

    Args:
        arg: The argument.

    Returns:
        prime_num.
    """
    if arg == 1:
        return 'no'
    for num in range(2, (arg // 2) + 1):
        if arg % num == 0:
            return 'no'
    return 'yes'


def calc():
    """Calc().

    Returns:
        correct answer.
    """
    rand_int1 = randint(0, 100)
    rand_int2 = randint(0, 100)
    rand_operator = choice(['+', '-', '*'])
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
    return correct_answer
