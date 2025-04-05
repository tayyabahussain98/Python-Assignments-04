

def get_first_element(lst):
    
    """
    Prints the first element of a provided list.
    """
    
    if len(lst) > 0:
        print(f'First Element: {lst[0]}')
    else:
        print('The list is empty! No first element.')


def get_lst():
    
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """

    lst = []
    elem: str = input('Please enter an element of the list or press enter to stop. ')
    while elem != '':
        lst.append(elem)
        elem: str = input('Please enter an element of the list or press enter to stop. ')
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()