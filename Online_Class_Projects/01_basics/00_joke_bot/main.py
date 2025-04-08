from colorama import Fore, init

init()

PROMPT: str = 'What do you want?'
JOKE: str = """Here is a joke for you!
Sophia is heading out to the grocery store.
A programmer tells her: 'Get a liter of milk, and if they have eggs, get 12'.
Sophia returns with 13 liters of milk.
The programmer asks: 'Why????' and
Sophia replies: 'Because they had eggs.'"""
SORRY: str = 'Sorry I only tell jokes!'

def main():

    """
    Main function to interact with the user and respond with a joke or an apology.
    Prompts the user for input and checks if the input contains the word "joke".
    If it does, it prints a joke in magenta color.
    Otherwise, it prints an apology in red color.
    The function uses color formatting from the `colorama` library.
    """

    try:
        user_input = input(f'{Fore.CYAN}{PROMPT}').strip().lower()

        if user_input == 'joke':
            print(f'{Fore.MAGENTA}{JOKE}')
        else:
            print(f'{Fore.RED}{SORRY}')
    except KeyboardInterrupt:
        print(f'{Fore.YELLOW}\nProgram cancelled by user. Goodbye!')


if __name__ == '__main__':
    main()