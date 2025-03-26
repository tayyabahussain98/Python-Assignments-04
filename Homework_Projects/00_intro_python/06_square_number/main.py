

def square():
    print('Calculate the Square of a Number!!')

    num: float = float(input('Type the number to see its square: '))

    print(f'{num} squared is {num ** 2}.')


if __name__ == '__main__':
    square()