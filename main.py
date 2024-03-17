import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Set up the screen
screen = turtle.Screen()

# Set up the screen
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)

# Create objects for snake, food, scoreboard, and game over screen
snake = Snake()
food = Food()
score = Scoreboard()


# Set up keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.08)  # Introduce a delay to control the snake's speed
    snake.move()  # Move the snake

    # Check if the snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.enlarge()
        score.clear()
        score.add_score()

    # Check if the snake hits the wall
    if (
            snake.head.xcor() > 290
            or snake.head.xcor() < -300
            or snake.head.ycor() > 300
            or snake.head.ycor() < -290
    ):
        score.clear()
        score.reset()
        snake.reset()

    # Check if the snake collides with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.clear()
            score.reset()
            snake.reset()

screen.exitonclick()  # Keep the window open until clicked
