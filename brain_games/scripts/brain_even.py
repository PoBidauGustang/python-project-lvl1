#!/usr/bin/env python3
"""Even game."""
from brain_games.games import even
from brain_games.games.engine import run


def main():
    """Welcome to the Brain Games, play brain-even."""
    run(even)


if __name__ == '__main__':
    main()
