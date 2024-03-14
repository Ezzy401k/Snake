import turtle

# Define constants for starting positions and movement
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Reference to the head segment of the snake

    def create_snake(self):
        # Create the initial segments of the snake
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def enlarge(self):
        # Add a new segment to the end of the snake
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
