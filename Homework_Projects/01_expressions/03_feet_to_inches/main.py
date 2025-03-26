

INCHES_IN_FEET: int = 12

def main():

     """
    Converts a measurement in feet to inches and prints the result.  
    Prompts the user to enter a number of feet, converts the input to inches,
    and prints the equivalent measurement in inches.
    """
     
     feet: float = float(input('Enter number of feet: '))
     inches: float = feet * INCHES_IN_FEET

     print(f'This is {inches} inches!')


if __name__ == '__main__':
     main()