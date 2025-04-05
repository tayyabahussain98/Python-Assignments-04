

def add_three_copies(my_list, data):

    """
    Appends the given data to the provided list three times.
    """

    for i in range(3):
        my_list.append(data)

def main():
    message = input('Enter a message to copy: ')
    my_list = []
    print(f'List before: {my_list}')
    add_three_copies(my_list, message)
    print(f'List after: {my_list}')


if __name__ == '__main__':
    main()


# Comparison with Immutable Data

def change(x):
    x = x + 3

num: int = 20
change(num)
print(num)