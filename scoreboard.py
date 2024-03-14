import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"score: {self.score}", False, "center", ("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.write(f"score: {self.score}", False, "center", ("Arial", 12, "normal"))
