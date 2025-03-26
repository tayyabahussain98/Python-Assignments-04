

def main():

    """
    This is the main function that performs integer division and calculates the remainder.  
    It prompts the user to input two integers: one to be divided and one to divide by.  
    It then calculates the quotient and the remainder of the division.  
    Finally, it prints the result of the division and the remainder.  
    """

    num_1: int = int(input('Please enter an integer to be divided: '))
    num_2: int = int(input('Please enter an integer to divide by: '))

    quotient: int = num_1 // num_2
    remainder: int = num_1 % num_2

    print(f'The result of this division is {quotient} with a remainder of {remainder}')


if __name__ == '__main__':
    main()