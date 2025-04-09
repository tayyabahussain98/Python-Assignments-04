import random

def guess(x):
    random_number: int = random.randint(1, x)
    guess: int = 0


    while guess != random_number:
        guess: int = int(input(f'Guess a number between 1 and {x}: '))
        
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

if __name__ == '__main__':
    guess(10)