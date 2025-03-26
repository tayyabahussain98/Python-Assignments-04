

def main():
    print('Simple program to convert Fahrenheit to Celsius')

    degrees_fahrenheit: float = float(input('Enter temperature in Fahreheit: '))

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius:.2f}°C")


if __name__ == '__main__':
    main()