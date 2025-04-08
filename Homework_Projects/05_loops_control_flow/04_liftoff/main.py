

import time

def main():

    """
    A program that prints out the calls for a spaceship that is about to launch.  
    Countdown from 10 to 1 and then output Liftoff!
    """

    print('🚀 Spaceship Launch Countdown Initiated!\n')


    for i in range(10, 0, -1):
        print(f'{i} 🔥', flush = True)
        time.sleep(0.5)

    print('\n')
    time.sleep(0.7)
    print('💥 💥 💥')
    time.sleep(0.5)
    print('🌟 Liftoff! 🌌✨\n')
    print('🚀 The spaceship is now in space. Great job, commander!')


if __name__ == '__main__':
    main()