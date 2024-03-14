import turtle


class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def game_end(self):
        self.write("Game Over!", False, "center", ("Arial", 14, "normal"))
