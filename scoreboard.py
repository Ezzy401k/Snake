import turtle

with open("high_score.txt") as file:
    content = int(file.read())


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (turtle.Turtle)
        self.score = 0  # Initialize the score to 0
        self.high_score = content
        self.color("white")  # Set the color of the turtle to white
        self.penup()  # Pen up to prevent drawing lines
        self.hideturtle()  # Hide the turtle initially
        self.goto(0, 280)  # Move the turtle to the specified position
        self.reset()
        # Write the initial score at the specified position using Arial font with size 12

    def add_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score
        self.write(f"score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 12, "normal"))
        # Write the updated score at the specified position using Arial font with size 12

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode= "w") as file:
                file.write(f"{self.high_score}")
        self.score = -1
        self.add_score()
