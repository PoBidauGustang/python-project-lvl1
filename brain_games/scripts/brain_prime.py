#!/usr/bin/env python3
"""Prime game."""
from brain_games.engine import run
from brain_games.games import prime


def main():
    """Welcome to the Brain Games, play brain-prime."""
    run(prime)


if __name__ == '__main__':
    main()
