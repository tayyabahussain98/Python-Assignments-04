

def add_many_numbers(numbers: list[int])->int:

    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total: int = 0
    for number in numbers:
        total += number

    return total

def main():
    numbers: list[int] = [2, 4, 6, 8, 10]
    sum_of_numbers: int = add_many_numbers(numbers)
    print(sum_of_numbers)


if __name__ == '__main__':
    main()