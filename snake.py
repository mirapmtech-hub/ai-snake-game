import curses
import random
import time

def game_loop(stdscr):
    # Initial settings
    curses.curs_set(0) # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(100) # Refresh every 100ms

    sh, sw = stdscr.getmaxyx()
    # Boundary check to avoid errors on small terminals
    if sh < 10 or sw < 20:
        stdscr.addstr(0, 0, "Terminal too small!")
        stdscr.refresh()
        time.sleep(2)
        return False # Don't restart

    # Create snake and food
    snake_x = sw // 4
    snake_y = sh // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Check for quit
        if key == ord('q'):
            return False

        # Calculate new head position
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Check for collisions with walls or self
        if (new_head[0] in [0, sh - 1] or 
            new_head[1] in [0, sw - 1] or 
            new_head in snake):
            # Game over message
            msg = "Game Over! Press 'q' to quit or any other key to restart."
            stdscr.addstr(sh // 2, (sw - len(msg)) // 2, msg)
            stdscr.refresh()
            stdscr.nodelay(0)
            ch = stdscr.getch()
            return ch != ord('q')

        # Insert new head
        snake.insert(0, new_head)

        # Check if snake ate the food
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            stdscr.addch(tail[0], tail[1], ' ')

        # Draw snake
        stdscr.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

if __name__ == "__main__":
    should_restart = True
    while should_restart:
        try:
            should_restart = curses.wrapper(game_loop)
        except KeyboardInterrupt:
            should_restart = False
