#!/usr/bin/env python3
"""Calculator game."""
from brain_games.games import calc
from brain_games.games.engine import run


def main():
    """Welcome to the Brain Games, play brain-calc."""
    run(calc)


if __name__ == '__main__':
    main()
