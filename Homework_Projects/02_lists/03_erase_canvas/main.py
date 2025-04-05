

import os
import time
import random

CANVAS_WIDTH: int = 10
CANVAS_HEIGHT: int = 10
ERASER_SIZE: int = 2


COLORS = ['🟦', '🟩', '🟨', '🟧', '🟥']


canvas = [[random.choice(COLORS) for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]

def print_canvas():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in canvas:
        print(' '.join(row))
    print('\nW/A/S/D to move, X to undo, Q to quit.')

def erase(x, y):
    for i in range(max(0, y), min(CANVAS_HEIGHT, y + ERASER_SIZE)):
        for j in range(max(0, x), min(CANVAS_WIDTH, x + ERASER_SIZE)):
            canvas[i][j] = '⬜'

def undo():
    for _ in range(3):
        x, y = random.randint(0, CANVAS_WIDTH - 1), random.randint(0, CANVAS_HEIGHT - 1)
        canvas[y][x] = random.choice(COLORS)

def main():
    eraser_x, eraser_y = CANVAS_WIDTH // 2, CANVAS_HEIGHT //2
    print_canvas()

    while True:
        command = input('Move (W/A/S/D), Undo (X), Quit (Q): ').strip().lower()
        if command == 'q':
            break
        elif command == 'w' and eraser_y > 0:
            eraser_y -= 1
        elif command == 's' and eraser_y < CANVAS_HEIGHT:
            eraser_y += 1
        elif command == 'a' and eraser_x > 0:
            eraser_x -= 1
        elif command == 'd' and eraser_x < CANVAS_WIDTH:
            eraser_x += 1
        elif command == 'x':
            undo()

        erase(eraser_x, eraser_y)
        print_canvas()
        time.sleep(0.1)


if __name__ == '__main__':
    main()