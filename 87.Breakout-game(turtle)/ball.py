from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """Initialize the Ball class."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -220)
        self.move_x = 5
        self.move_y = 5
        self.spd = 1

    def move(self):
        """Move the ball based on its current speed and direction."""
        self.new_x = self.xcor() + self.move_x
        self.new_y = self.ycor() + self.move_y
        self.goto(self.new_x, self.new_y)

    def change_x(self):
        """Change the horizontal direction of the ball."""
        self.move_x = -1 * self.move_x

    def change_y(self):
        """Change the vertical direction of the ball."""
        self.move_y = -1 * self.move_y
