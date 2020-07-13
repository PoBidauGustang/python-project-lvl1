#!/usr/bin/env python3
"""Gcd game."""
from brain_games.games import gcd
from brain_games.games.engine import run


def main():
    """Welcome to the Brain Games, play brain-gcd."""
    run(gcd)


if __name__ == '__main__':
    main()
