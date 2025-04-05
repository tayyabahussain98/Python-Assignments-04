
def get_last_element(lst):

    """
    Prints the last element of the provided list.
    """
    if len(lst) > 0:
        print(f'Last Element: {lst[-1]}')
    else:
        print('The list is empty! No last element.')

def get_lst():
    lst = []
    elem: str = input('Please enter an element of the list or press enter to stop. ')
    while elem != '':
        lst.append(elem)
        elem: str = input('Please enter an element of the list or press enter to stop. ')
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()