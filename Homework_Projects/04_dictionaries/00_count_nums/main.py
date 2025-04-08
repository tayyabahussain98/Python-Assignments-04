

def get_user_numbers() -> list[int]:
    user_numbers: list[int] = []
    while True:
        user_input: str = input('Enter a number: ')
        if not user_input:
            break
        num: int = int(user_input)
        user_numbers.append(num)
    return user_numbers

def count_nums(num_list: list[int]) -> dict[int, int]:
    num_dict: dict[int, int] = {}
    for num in num_list:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


def print_counts(num_dict: dict[int, int]) -> None:
    for num in num_dict:
        print(f'{num} appears {num_dict[num]} times.')


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


if __name__ == '__main__':
    main()