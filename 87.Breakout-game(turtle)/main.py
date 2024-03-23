from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Brick
from ball import Ball
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Breakout Game")
screen.tracer(0)

# Initialize game objects
paddle = Paddle()
brick_instance = Brick()
ball = Ball()
scoreboard = Scoreboard()
scoreboard.display_lives()

# Set up key listeners
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.update()
screen.tracer(1)

game_end = False

while not game_end:
    # Move the ball
    ball.move()

    # Collision with the walls
    if ball.xcor() < -270 or ball.xcor() > 270:
        ball.change_x()
    if ball.ycor() > 270:
        ball.change_y()

    # Collision with bricks
    for brick in brick_instance.bricks:
        if ball.distance(brick) < 50:
            # Update score and brick wall
            scoreboard.score += 1
            brick_instance.update_brick_wall(brick)
            ball.change_y()

        if ball.distance(brick) < 50 and brick.ycor() - 10 < ball.ycor() < brick.ycor() + 10:
            ball.change_x()

    # Collision with paddle
    if ball.distance(paddle) < 20:
        ball.change_x()
        ball.change_y()

    # Check if ball goes below the paddle
    if ball.ycor() < -280:
        ball.hideturtle()
        screen.tracer(0)
        ball = Ball()
        paddle.goto(x=0, y=-240)
        screen.update()
        screen.tracer(1)
        scoreboard.lives -= 1
        scoreboard.display_lives()

    # Check if no lives left
    if scoreboard.lives == 0:
        game_end = True
        scoreboard.display_result()
        scoreboard.display_score()

screen.exitonclick()
