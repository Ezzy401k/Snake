import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (turtle.Turtle)
        self.score = 0  # Initialize the score to 0
        self.color("white")  # Set the color of the turtle to white
        self.penup()  # Pen up to prevent drawing lines
        self.hideturtle()  # Hide the turtle initially
        self.goto(0, 280)  # Move the turtle to the specified position
        self.write(f"score: {self.score}", False, "center", ("Arial", 12, "normal"))
        # Write the initial score at the specified position using Arial font with size 12

    def add_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score
        self.write(f"score: {self.score}", False, "center", ("Arial", 12, "normal"))
        # Write the updated score at the specified position using Arial font with size 12
