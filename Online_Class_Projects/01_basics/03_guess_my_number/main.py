import random

FIRST_QUESTION: str = 'Enter a number: '
SECRET_NUMBER: int = random.randint(1, 99)

def main():

    print(f'\n{'-'*11} Number Guessing Game {'-'*11}')
    print("I'm thinking of a number between 1 and 99...")

    while True:
        user_input: str = input(FIRST_QUESTION)

        if not user_input:
            print('Existing the game. GoodBye!')
            break

        try:
            guess: int = int(user_input)
        except ValueError:
            print('❌ Please enter a valid number.')
            continue

        if guess > SECRET_NUMBER:
            print('Your guess is too high.\n')

        elif guess < SECRET_NUMBER:
            print('Your guess is too low.\n')
            
        else:
            print(f'Congrats! The number was: {SECRET_NUMBER}\n')
            break


if __name__ == '__main__':
    main()