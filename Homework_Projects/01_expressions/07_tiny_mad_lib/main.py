
def main():
    print('Mad Lib Program!!!!')

    noun: str = input('Noun: ')
    verb: str = input('Verb: ')
    adjective: str = input('Adjective: ')
    verb_2: str = input('Verb: ')

    madlib: str = f"""Learning a {verb.lower()} is very {adjective.lower()}.
{noun.capitalize()} can be difficult, so you need to {verb_2.lower()} hard."""
    
    print(madlib)


if __name__ == '__main__':
    main()