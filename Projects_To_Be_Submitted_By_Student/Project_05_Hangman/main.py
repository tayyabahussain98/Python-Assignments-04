import random
from words import words
import string


def get_valid_word(words):
    word: str = random.choice(words)    # Randomly chooses something from the list

    while '-' in word or ' ' in word:
        word: str = random.choice(words)

    return word

def hangman():
    word: str = get_valid_word(words).upper()
    word_letters: str = set(word)   # Letters in the word
    alphabet: str = set(string.ascii_uppercase)
    used_letters: str = set()    # What the user have guessed
    lives: int = 6

    print("Let's play Hangman!")

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) ==> 'a b cd'
        print(f'\nYou have {lives} lives left.')
        print('You have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter: str = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f'Wrong! {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')

    # Gets here when len(word_letters) == 0 OR when lives == 0

    if lives == 0:
        print(f'Sorry, you died. The word was {word}')
    else:
        print(f'Yay! You guessed the word {word} correctly! 🎉')

    


if __name__ == '__main__':
    hangman()