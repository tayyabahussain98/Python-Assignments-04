
MAX_LENGTH: int = 3

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed element.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f'Removing: {removed_item}')

def get_lst():
    lst = []
    elem: str = input('Please enter an element of the list or press enter to stop. ')
    while elem != '':
        lst.append(elem)
        elem: str = input('Please enter an enter of the list or press enter to stop. ')
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print(f'Final list: {lst}')

if __name__ == '__main__':
    main()