import turtle
import time
from snake import Snake  # Assuming 'snake' is a class or function defined in a module called 'snake'

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)  # Turn off animation

# Create a Snake object
snake = Snake()

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
    time.sleep(0.1)  # Introduce a delay to control the snake's speed

    snake.move()  # Move the snake

screen.exitonclick()  # Keep the window open until clicked
