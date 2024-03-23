from turtle import Turtle, Screen
from scoreboard import Scoreboard
from alien import Alien
from bunker import Bunker
from shooter import Shooter
from collision_detector import CollisionDetector
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("My Space Invaders Game")

screen.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
scoreboard = Scoreboard()
alien = Alien()
bunker = Bunker()
shooter = Shooter()
collision_detector = CollisionDetector()

# Design background
turtle = Turtle()
turtle.pencolor("springgreen")
turtle.pensize(2)
turtle.penup()
turtle.hideturtle()
turtle.goto(-300, -290)
turtle.pendown()
turtle.forward(600)

screen.update()

# Set up key listeners
screen.listen()
screen.onkey(shooter.move_left, "Left")
screen.onkey(shooter.move_right, "Right")
screen.onkey(shooter.create_laser, "L")

game_end = False
while not game_end:
    screen.update()  # Update the screen manually

    # Move aliens at regular intervals
    screen.ontimer(alien.move_aliens(), 1000)

    # Move shooter bullets
    shooter.shoot()

    # Check for collisions with aliens
    if collision_detector.laser_alien(shooter, alien):
        scoreboard.score += 1
        scoreboard.update_score()

    # Check for collisions with bunker
    collision_detector.laser_bunker(shooter, bunker)
    collision_detector.bullet_bunker(bunker, alien)

    # Check for collisions of laser with bullet
    collision_detector.laser_bullet(shooter, alien)

    # Check if shooter is hit by alien bullets
    if not collision_detector.bullet_shooter(alien, shooter):
        scoreboard.game_over_msg()

# This code is currently an infinite loop and will never reach here
screen.exitonclick()
