"""Game engine."""
from random import randint

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


def gcd(arg1, arg2):
    """Give gcd of two integers.

    Args:
        arg1: The first argument.
        arg2: The second argument.

    Returns:
        grand_cd.
    """
    while arg2 != 0:
        var_help = arg2
        arg2 = arg1 % arg2
        arg1 = var_help
    return arg1


def progression():
    """Progression().

    Returns:
        progress.
    """
    num = randint(1, 10)
    progress = list(range(num, (10 * num) + 1, num))
    return progress


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
