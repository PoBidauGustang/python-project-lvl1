"""Game engine."""
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
