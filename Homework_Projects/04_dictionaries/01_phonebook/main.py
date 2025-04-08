

def create_phonebook():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """

    phonebook = {}

    while True:
        name: str = input('Name: ')

        if not name:
            break
        number: str = input('Number: ')
        phonebook[name] = number

    return phonebook

def display_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    
    print('\nPhonebook Entries:')
    for name in phonebook:
        print(f'{name} -> {phonebook[name]}')

def lookup_phonebook(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        lookup_name: str = input('\nEnter a name to lookup: ')

        if not lookup_name:
            break

        if lookup_name not in phonebook:
            print(f'{lookup_name} is not in the phonebook.')
        else:
            print(f"{lookup_name}'s number is {phonebook[lookup_name]}")

def main():
    phonebook = create_phonebook()
    display_phonebook(phonebook)
    lookup_phonebook(phonebook)


if __name__ == '__main__':
    main()