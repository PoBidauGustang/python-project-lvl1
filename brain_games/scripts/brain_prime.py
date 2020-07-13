#!/usr/bin/env python3
"""Prime game."""
from brain_games.games import prime
from brain_games.games.engine import run


def main():
    """Welcome to the Brain Games, play brain-prime."""
    run(prime)


if __name__ == '__main__':
    main()
