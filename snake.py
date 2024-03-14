import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Starting positions for the snake segments
MOVE_DISTANCE = 20  # Distance to move in each step
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHT = 0  # Angle for moving right


class Snake:
    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Create the snake
        self.head = self.segments[0]  # Reference to the head segment of the snake

    def create_snake(self):
        # Create the snake segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def enlarge(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake forward
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change the snake's direction to up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # Change the snake's direction to right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # Change the snake's direction to left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
