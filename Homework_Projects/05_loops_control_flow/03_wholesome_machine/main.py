
AFFIRMATION: str = "I'm capable of doing anything. I put my mind to."


def main():

    """
    A program which prompts the user to type an affirmation of your choice until they type it correctly.
    """

    print(f'Please type the following affirmation: {AFFIRMATION}')

    while True:
        user_input: str = input()

        if user_input == AFFIRMATION:
            print("That's right!")
            break
        else:
            print(f'That was not the affirmation. Please type the following affirmation: {AFFIRMATION}')


if __name__ == '__main__':
    main()