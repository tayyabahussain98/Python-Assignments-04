
def check_height(height):
    MINIMUM_HEIGHT: int = 50

    """
    Checks if a person is tall enough to ride based on the minimum height.
    """

    if height >= MINIMUM_HEIGHT:
        return "You're tall enough to ride!"
    else:
        return "You're not tall enough to ride, but maybe next year!"

def main():
    while True:
        user_input: str = input('How tall are you? ')

        if not user_input:
            break

        height: int = int(user_input)

        message = check_height(height)

        print(message)


if __name__ == '__main__':
    main()