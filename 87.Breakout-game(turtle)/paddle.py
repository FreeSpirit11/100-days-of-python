from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        """Initialize the Paddle class."""
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        """Create and configure the paddle."""
        self.shape("square")
        self.color("grey")
        self.shapesize(0.7, 4.5, 4)
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=-240)

    def move_right(self):
        """Move the paddle to the right."""
        self.forward(20)

    def move_left(self):
        """Move the paddle to the left."""
        self.backward(20)

    def refresh(self):
        """Clear the paddle and recreate it."""
        self.clear()
        self.create_paddle()
