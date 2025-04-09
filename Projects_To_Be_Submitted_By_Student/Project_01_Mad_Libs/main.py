
def main():
    print('\n👩‍💻 Welcome to the Programming Madlib Game!')
    print('👉 Fill in the blanks to create your custom coding story!\n')


    name: str = input('Enter your name: ')
    language: str = input('Enter a programming language: ')
    adjective: str = input('Enter an adjective: ')
    noun: str = input('Enter a noun: ')
    verb: str = input('Enter a verb (present tense): ')
    famous_dev: str = input('Nme of a famous developer or Youtuber: ')
    error: str = input('Type of programming eror (e.g., SyntaxError): ')
    emotion: str = input('An emotion: ')

    print('\n🛠️ Generating your coding story...\n')

    story: str = f'''
Once upon a time, there was a passionate code named {name}.
{name} decided to learn {language}, and it turned out to be a {adjective} journey.
    
    
One day, while working on a {noun}, they tried to {verb}, but suddenly an error popped up: {error}!
{name} felt very {emotion}, but did'nt give up.
    
    
After watching some tutorials by {famous_dev}, everything started making sense.
Eventually, {name} fixed the error, completed the project, and became a {adjective} {language} developer!
    
    
🎉 The End - Keep coding and never give up like {name}!
'''

    print(story)


if __name__ == '__main__':
    main()