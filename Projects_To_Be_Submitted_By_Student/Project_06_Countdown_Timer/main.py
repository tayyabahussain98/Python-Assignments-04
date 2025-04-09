import time
import sys

def countdown(total_seconds):
    try:
        print('⌛ Starting teh timer...\n')
        while total_seconds:
            mins, secs = divmod(total_seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f'\r⏲ Time left: {timer }', end = '', flush = True)
            time.sleep(1)
            total_seconds -= 1


        print('\n✅ Timer completed!')

        # Adding a finishing up progress effect
        print('⏱ Finalizing...', end = '')
        for _ in range(5):
            print('.', end = '', flush = True)
            time.sleep(0.5)
        print("\n🎉 Time's up! Take a break or switch task.")

    except KeyboardInterrupt:
        print('\n⛔ Timer interrupted by user.')

def get_seconds():
    '''Get valid input from user for the timer.'''
    while True:
        try:
            mins: int = int(input('⏲ Enter minutes: '))
            secs: int = int(input('Enter seconds: '))
            total_time = mins * 60 + secs
            if total_time <= 0:
                print('❌ Please enter a positive time value.')
            else:
                return total_time
            
        except ValueError:

            print('❌ Please enter valid numeric values.')
            continue


if __name__ == '__main__':
    total_time = get_seconds()  # Get user input for time in seconds
    countdown(total_time)   # Start countdown with the given time