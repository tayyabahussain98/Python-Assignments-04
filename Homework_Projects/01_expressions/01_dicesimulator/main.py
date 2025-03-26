"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random

NUM_SIDES: int = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """

    die_1: int = random.randint(1, NUM_SIDES)
    die_2: int = random.randint(1, NUM_SIDES)

    total: int = die_1 + die_2

    print(f'Total of two dice: {total}')

def main():
    die_1: int = 10

    print(f'{die_1} in main() starts as: {die_1}')
    roll_dice()
    roll_dice()
    roll_dice()
    print(f'{die_1} in main() is: {die_1}')


if __name__ == '__main__':
    main()