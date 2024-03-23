from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """
        Initialize the Scoreboard object.

        This method sets up the Scoreboard attributes, such as the initial
        score, and calls the display_score method to show the score on the
        screen.
        """
        super().__init__()
        self.score = 0
        self.display_score()

    def display_score(self):
        """
        Display the current score on the screen.

        This method clears the previous score, sets up the turtle properties,
        and writes the current score on the screen.
        """
        self.clear()
        self.hideturtle()
        self.penup()
        self.pencolor("springgreen")
        self.goto(200, -320)
        self.pendown()
        self.write(f"Score: {self.score}", font=("Arial", 22, "normal"))

    def update_score(self):
        """
        Update and display the current score.

        This method clears the previous score and writes the updated score on
        the screen.
        """
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 22, "normal"))

    def game_over_msg(self):
        """
        Display the game over message.

        This method clears the screen, sets up the turtle position, and writes
        the game over message along with the final score in the center of the
        screen.
        """
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over.\nScore: {self.score}", font=("Arial", 42, "normal"), align="center")
