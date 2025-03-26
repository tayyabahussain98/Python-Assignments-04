

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random

NUM_SIDES: int = 6

def main():
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    # If you use the same seed value you will get the same random number.

    die_1: int = random.randint(1, NUM_SIDES)
    die_2: int = random.randint(1, NUM_SIDES)

    total: int = die_1 + die_2

    print(f'Dice have {NUM_SIDES} sides each.')
    print(f'First die: {die_1}')
    print(f'Second die: {die_2}')
    print(f'Total of two dice: {total}')


if __name__ == '__main__':
    main()