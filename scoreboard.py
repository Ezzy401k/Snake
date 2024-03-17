import turtle

# Read the high score from a file
with open("high_score.txt") as file:
    content = int(file.read())

# Define the Scoreboard class
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()  # Initialize the parent class (turtle.Turtle)
        self.score = 0  # Initialize the score to 0
        self.high_score = content  # Set the high score from the file
        self.color("white")  # Set the color of the turtle to white
        self.penup()  # Pen up to prevent drawing lines
        self.hideturtle()  # Hide the turtle initially
        self.goto(0, 280)  # Move the turtle to the specified position
        self.reset()  # Call the reset method to initialize the scoreboard

    def add_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score
        # Write the updated score and high score at the specified position using Arial font with size 12
        self.write(f"score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 12, "normal"))

    def reset(self):
        # Check if the current score is greater than the high score
        if self.score > self.high_score:
            self.high_score = self.score  # Update the high score
            # Write the new high score to the file
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = -1  # Reset the score to -1
        self.add_score()  # Call the add_score method to update the display
