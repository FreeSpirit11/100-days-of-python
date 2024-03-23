from turtle import Turtle
import random

# List of colors for bricks
colours = [
    "blue", "red", "green", "grey", "orange", "purple", "pink", "brown",
    "cyan", "magenta", "yellow", "teal", "violet", "indigo", "lime", "olive",
    "maroon", "navy", "peru", "plum", "salmon", "sienna", "silver", "tan",
    "thistle", "tomato", "turquoise", "wheat", "yellowgreen", "darkgreen",
    "darkorange", "darkslategray", "darkturquoise", "darkviolet", "deeppink",
    "gold", "khaki", "lightcoral", "lightgreen", "lightskyblue", "mediumaquamarine"
]

class Brick:
    def __init__(self):
        """Initialize the Brick class."""
        self.bricks = []
        self.create_brick_wall()

    def add_brick(self):
        """Add a new brick to the list."""
        brick = Turtle(shape='square')
        brick.shapesize(1, 4.6, 4)
        brick.color(random.choice(colours))
        brick.penup()
        self.bricks.append(brick)

    def create_brick_wall(self):
        """Create a wall of bricks."""
        for _ in range(60):
            self.add_brick()
        i = 0
        j = 0
        col = 0
        for brick in self.bricks:
            col += 1
            brick.goto(x=-247+i, y=310-j)
            i += 97
            if col % 6 == 0:
                j += 25
                i = 0

    def update_brick_wall(self, brick_to_be_deleted: Turtle):
        """Update the brick wall by removing a brick."""
        self.bricks.remove(brick_to_be_deleted)
        brick_to_be_deleted.clear()
        brick_to_be_deleted.hideturtle()
