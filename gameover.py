import turtle


class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (turtle.Turtle)
        self.color("white")  # Set the color of the turtle to white
        self.hideturtle()  # Hide the turtle initially

    def game_end(self):
        self.write("Game Over!", False, "center", ("Arial", 14, "normal"))
        # Write "Game Over!" at the center of the screen using Arial font with size 14
