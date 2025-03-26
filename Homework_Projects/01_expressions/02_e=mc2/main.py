

Speed_Of_Light: int = 299792458


def Einstein_Equation():
    
    """
    Calculates the energy equivalent of a given mass using the formula E=mc^2.  
    Prompts the user to input a mass in kilograms, then calculates the energy
    using the speed of light constant and prints the result.
    """

    mass: float = float(input('Enter kilos of mass: '))

    energy: float = mass * (Speed_Of_Light ** 2)

    print('\ne = m * C^2...')
    print(f'\nm = {mass} kg')
    print(f'\nC = {Speed_Of_Light} m/s')

    print(f'\n{energy} joules of energy!')


if __name__ == '__main__':
    Einstein_Equation()