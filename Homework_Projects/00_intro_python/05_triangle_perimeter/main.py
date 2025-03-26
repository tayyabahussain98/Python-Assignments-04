

def calculate():
    print('Welcome to the Triangle Perimeter Calculator!!!')

    side_1: float = float(input('What is the length of side 1? '))
    side_2: float = float(input('What is the length of side 2? '))
    side_3: float = float(input('What is the length of side 3? '))

    perimeter: float = side_1 + side_2 + side_3

    print(f'The perimeter of the triangle is {perimeter}')


if __name__ == '__main__':
    calculate()