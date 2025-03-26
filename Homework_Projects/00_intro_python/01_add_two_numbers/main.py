
"""Another python program to get some practice with
variables.  This program asks the user for two
integers and prints their sum.
"""

def add():
    print('This program adds two numbers.')
    num_1: str = input('Enter first number: ')
    num_1: int = int(num_1)
    num_2: str = input('Enter your second number: ')
    num_2: int = int(num_2)
    total: int = num_1 + num_2

    print(f'The total is {total}.')


if __name__ == '__main__':
    add()