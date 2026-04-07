import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

FPS = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)

snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)


def spawn_food():
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE)
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)


food = spawn_food()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    if (
        new_head[0] < 0
        or new_head[0] >= WIDTH // CELL_SIZE
        or new_head[1] < 0
        or new_head[1] >= HEIGHT // CELL_SIZE
    ):
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        food = spawn_food()
    else:
        snake.pop()

    screen.fill(BLACK)

    pygame.draw.rect(
        screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

    score = len(snake) - 3
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
print(f"Game Over! Final Score: {len(snake) - 3}")
