import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (turtle.Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Pen up to prevent drawing lines
        self.shapesize(0.5, 0.5)  # Resize the food shape
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the animation speed to fastest
        self.refresh()  # Call the refresh method to position the food randomly

    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen boundaries
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen boundaries
        self.goto(random_x, random_y)  # Move the food to the randomly generated coordinates
