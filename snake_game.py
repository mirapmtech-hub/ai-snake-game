import curses
import random


def main(screen):
    curses.curs_set(0)
    sh, sw = screen.getmaxyx()
    window = curses.newwin(sh, sw, 0, 0)
    window.keypad(True)
    window.timeout(100)

    snake_x = sw // 4
    snake_y = sh // 2
    snake = [(snake_y, snake_x), (snake_y, snake_x - 1), (snake_y, snake_x - 2)]

    food = ()
    while True:
        new_food = (random.randint(1, sh - 1), random.randint(1, sw - 1))
        if new_food not in snake:
            food = new_food
            break

    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()
        if next_key != -1:
            if next_key == curses.KEY_DOWN and key != curses.KEY_UP:
                key = curses.KEY_DOWN
            elif next_key == curses.KEY_UP and key != curses.KEY_DOWN:
                key = curses.KEY_UP
            elif next_key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
                key = curses.KEY_LEFT
            elif next_key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
                key = curses.KEY_RIGHT

        head_y, head_x = snake[0]

        if key == curses.KEY_DOWN:
            head_y += 1
        elif key == curses.KEY_UP:
            head_y -= 1
        elif key == curses.KEY_LEFT:
            head_x -= 1
        elif key == curses.KEY_RIGHT:
            head_x += 1

        new_head = (head_y, head_x)

        if head_y == 0 or head_y == sh - 1 or head_x == 0 or head_x == sw - 1:
            break

        if new_head in snake:
            break

        snake.insert(0, new_head)

        if new_head == food:
            food = ()
            while food == ():
                new_food = (random.randint(1, sh - 1), random.randint(1, sw - 1))
                if new_food not in snake:
                    food = new_food
        else:
            snake.pop()

        window.clear()
        window.border()
        window.addch(food[0], food[1], "*")
        for y, x in snake:
            window.addch(y, x, "#")
        window.refresh()

    curses.endwin()
    print(f"Game Over! Your score: {len(snake) - 3}")


if __name__ == "__main__":
    curses.wrapper(main)
