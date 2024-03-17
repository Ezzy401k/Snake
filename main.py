import turtle
import time
from snake import Snake  # Import the Snake class from the snake module
from food import Food  # Import the Food class from the food module
from scoreboard import Scoreboard  # Import the Scoreboard class from the scoreboard module

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)  # Turn off automatic screen updates

# Create objects for snake, food, scoreboard, and game over screen
snake = Snake()  # Create a Snake object
food = Food()  # Create a Food object
score = Scoreboard()  # Create a Scoreboard object

# Set up keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.08)  # Introduce a delay to control the snake's speed
    snake.move()  # Move the snake

    # Check if the snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new position
        snake.enlarge()  # Increase the length of the snake
        score.clear()  # Clear the previous score display
        score.add_score()  # Update and display the score

    # Check if the snake hits the wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -290
    ):
        score.clear()  # Clear the previous score display
        score.reset()  # Reset the score to zero
        snake.reset()  # Reset the snake position and length

    # Check if the snake collides with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.clear()  # Clear the previous score display
            score.reset()  # Reset the score to zero
            snake.reset()  # Reset the snake position and length

screen.exitonclick()  # Keep the window open until clicked
