
import random

def guess_my_number():
    secret_number: int = random.randint(0, 99)

    print(f"\n{'-'*11} Number Guessing Game {'-'*11}")
    print("I'm thinking of a number between 0 and 99...")

    while True:
        user_input: str = input('Enter a guess: ')

        if not user_input:
            print('Existing the game. Goodbye!')
            break

        try:
            guess: int = int(user_input)
        except ValueError:
            print('❌ Please enter a valid number.')
            continue

        if guess > secret_number:
            print('Your guess is too high.\n')

        elif guess < secret_number:
            print('Your guess is too low.\n')

        else:
            print(f'Congrats! The number was: {secret_number}\n')
            break

if __name__ == '__main__':
    guess_my_number()