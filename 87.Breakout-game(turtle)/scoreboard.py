from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the Scoreboard class."""
        super().__init__()
        self.score = 0
        self.lives = 3
        self.pencolor("white")
        self.penup()
        self.hideturtle()

    def display_score(self):
        """Display the current score."""
        self.goto(0, -70)
        self.pendown()
        self.write(f"\nScore: {self.score}/60", align="center", font=("Arial", 30, "normal"))
        self.penup()

    def display_result(self):
        """Display the game over message."""
        self.goto(0, -30)
        self.pendown()
        self.write(f"Game Over.", align="center", font=("Arial", 40, "normal"))
        self.penup()

    def display_lives(self):
        """Display the remaining lives."""
        self.clear()
        self.goto(0, -280)
        self.pendown()
        self.write(f"Lives Remaining : {self.lives}", align="center", font=("Arial", 30, "normal"))
        self.penup()
