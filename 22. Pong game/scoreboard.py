from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.pendown()
        self.pencolor("white")

    def increase_score(self):
        self.clear()
        self.score+=1
    def display_score(self):
        self.write(self.score, align="center", font=("ariabic", 24, "normal"))
    def score_written(self):
        self.write("score", align="center", font=("ariabic", 24, "normal"))
    def game_over(self):
        self.write("Game Over", align="center", font=("ariabic", 24, "normal"))


