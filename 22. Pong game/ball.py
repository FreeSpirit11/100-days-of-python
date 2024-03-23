from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 5
        self.move_y = 5
        self.spd=0.04

    def move(self):
        self.new_x = self.xcor() + self.move_x
        self.new_y = self.ycor() + self.move_y
        self.goto(self.new_x, self.new_y)

    def xmove(self):
        self.move_x=-1*self.move_x

    def ymove(self):
        self.move_y = -1 * self.move_y
    def sped(self):
        self.spd*0.000000001





