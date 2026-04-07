import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=400)
screen.tracer(0)

# Colors
GREEN = "green"
RED = "red"
BLACK = "black"
WHITE = "white"

# Create snake head
head = turtle.Turtle()
head.shape("square")
head.color(GREEN)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create food
food = turtle.Turtle()
food.shape("circle")
food.color(RED)
food.penup()
food.goto(0, 100)

# Score
score = 0
high_score = 0

# Score display
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.penup()
score_board.goto(0, 180)
score_board.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Game over message
game_over_text = turtle.Turtle()
game_over_text.hideturtle()

# Snake body segments
segments = []


# Change direction
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Move snake
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# Keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check wall collision
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 190
        or head.ycor() < -190
    ):
        game_over_text.penup()
        game_over_text.goto(0, 0)
        game_over_text.write(
            "Game Over! Press Space to restart",
            align="center",
            font=("Arial", 20, "bold"),
        )
        screen.onkeypress(lambda: None, "space")
        screen.mainloop()

    # Check food collision
    if head.distance(food) < 15:
        # Move food to new spot
        food.goto(random.randint(-270, 270), random.randint(-170, 170))

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color(GREEN)
        new_segment.penup()
        segments.append(new_segment)

        # Increase score
        score += 10
        score_board.clear()
        score_board.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

    # Move body segments
    for i in range(len(segments) - 1, -1, -1):
        if i == 0:
            segments[i].goto(head.xcor(), head.ycor())
        else:
            segments[i].goto(segments[i - 1].xcor(), segments[i - 1].ycor())

    move()

    # Check self collision
    for segment in segments:
        if head.distance(segment) < 15:
            game_over_text.penup()
            game_over_text.goto(0, 0)
            game_over_text.write(
                "Game Over! Press Space to restart",
                align="center",
                font=("Arial", 20, "bold"),
            )
            screen.mainloop()

    time.sleep(0.1)
