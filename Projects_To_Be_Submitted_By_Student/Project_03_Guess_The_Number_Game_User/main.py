import random



def computer_guess(x):
    low: int = 1
    high: int = x
    feedback: str = ''
    attempts: int = 0

    while feedback != 'c' and low != high:
        if low != high:
            guess: int = random.randint(low, high)
        
        else:
            guess = low     # Could also be high b/c low = high
        
        feedback: str = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        attempts += 1   # Count each attempt

        if feedback == 'h':
            high: int = guess - 1

        elif feedback == 'l':
            low: int = guess + 1

    
    print(f'Yay! The computer guessed your number, {guess}, correctly!!')
    print(f'It took {attempts} attempts!')  	# Display the number of attempts



if __name__ == '__main__':
    computer_guess(1000)