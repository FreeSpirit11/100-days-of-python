from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball=Ball()
l_scoreboard=Scoreboard((-40,230))
r_scoreboard=Scoreboard((40,230))
scoreboard=Scoreboard((0,260))
scoreboard.score_written()

screen.listen()
screen.onkey(l_paddle.move_up, "A")
screen.onkey(l_paddle.move_down, "Z")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

turtle=Turtle()
turtle.penup()
turtle.color("white")
turtle.goto(390,290)
turtle.pendown()
turtle.pencolor("white")
turtle.setheading(-90)
turtle.forward(581)
turtle.setheading(180)
turtle.forward(787)
turtle.setheading(90)
turtle.forward(589)
turtle.setheading(0)
turtle.forward(780)
turtle=Turtle()
turtle.hideturtle()
turtle.setheading(90)
turtle.color("white")
turtle.forward(299)
turtle=Turtle()
turtle.hideturtle()
turtle.setheading(-90)
turtle.color("white")
turtle.forward(291)

screen.update()
finalee=Scoreboard((0,0))

game_is_on = True
while game_is_on:
    time.sleep(ball.spd)
    screen.update()
    l_scoreboard.display_score()
    r_scoreboard.display_score()

    ball.move()
    if ball.ycor()>=289 or ball.ycor()<=-281:
        ball.ymove()

    elif 345>ball.xcor()>=340 and ball.distance(r_paddle)<=50 :
        ball.xmove()
        r_scoreboard.increase_score()
        ball.sped()
    elif -345<ball.xcor()<=-340 and ball.distance(l_paddle)<=50:
        ball.xmove()
        l_scoreboard.increase_score()
        ball.sped()

    elif ball.xcor()>400 :
        ball.hideturtle()
        ball.penup()
        ball.goto(0,0)
        ball.showturtle()
        l_scoreboard.increase_score()
        ball.xmove()
    elif ball.xcor()<-400:
        ball.hideturtle()
        ball.penup()
        ball.goto(0, 0)
        ball.showturtle()
        r_scoreboard.increase_score()
        ball.xmove()







screen.exitonclick()
