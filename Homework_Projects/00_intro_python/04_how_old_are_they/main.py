

def ages():

    """
    This program calculates and prints the ages of five friends: Anton, Beth, Chen, Drew, and Ethan.

    Anton is 21 years old.  
    Beth is 6 years older than Anton.  
    Chen is 20 years older than Beth.  
    Drew is as old as Chen's age plus Anton's age.  
    Ethan is the same age as Chen.
    
    The program stores each person's age in a variable and prints their names and ages.
    """

    anthon_age: int = 21
    beth_age: int = 6 + anthon_age
    chen_age: int = 20 + beth_age
    drew_age: int = chen_age + anthon_age
    ethan_age: int = chen_age
    
    print(f'Anthon is {anthon_age}')
    print(f'Beth is {beth_age}')
    print(f'Chen is {chen_age}')
    print(f'Drew is {drew_age}')
    print(f'Ethan is {ethan_age}')


if __name__ == '__main__':
    ages()