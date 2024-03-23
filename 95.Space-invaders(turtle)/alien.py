from turtle import Turtle
import random

class Alien:
    def __init__(self):
        """
        Initialize the Alien class.

        Attributes:
            aliens (list): List to store alien turtles.
            bullets (list): List to store bullet turtles.
            sparks (list): List to store spark turtles.
            move_right (bool): Flag to determine the direction of alien movement.

        Methods:
            add_alien(i, j): Add an alien turtle at the specified position.
            create_aliens(): Create a grid of alien turtles.
            move_aliens(): Move the aliens and handle firing bullets.
            create_spark(x, y): Create a spark turtle at the specified position.
            fire_bullet(alien): Fire a bullet from the specified alien.
            move_bullets(): Move the bullets.
        """
        self.aliens = []
        self.bullets = []
        self.sparks = []
        self.move_right = True
        self.create_aliens()

    def add_alien(self, i, j):
        """
        Add an alien turtle at the specified position.

        Args:
            i (int): X-coordinate.
            j (int): Y-coordinate.
        """
        alien = Turtle(shape="square")
        alien.color("red")
        alien.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=3)
        alien.penup()
        self.aliens.append(alien)
        alien.goto(-250 + i, 300 - j)

    def create_aliens(self):
        """
        Create a grid of alien turtles.
        """
        j = 0
        for row in range(5):
            i = 0
            j += 20
            for col in range(11):
                i += 25
                self.add_alien(i, j)

    def move_aliens(self):
        """
        Move the aliens and handle firing bullets.
        """
        if self.sparks:
            for spark in self.sparks:
                spark.clear()
                spark.hideturtle()
        self.sparks.clear()
        self.move_bullets()
        if self.aliens[0].xcor() > 10:
            self.move_right = False
        elif self.aliens[0].xcor() < -280:
            self.move_right = True

        for alien in self.aliens:
            if self.move_right:
                alien.forward(20)
            else:
                alien.backward(20)
            if random.randint(0, 100) == 0:
                self.fire_bullet(alien)

    def create_spark(self, x, y):
        """
        Create a spark turtle at the specified position.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.

        Returns:
            Turtle: Spark turtle.
        """
        spark = Turtle()
        spark.shape("circle")
        spark.color("white")
        spark.shapesize(0.5)
        spark.penup()
        spark.goto(x, y)
        return spark

    def fire_bullet(self, alien: Turtle):
        """
        Fire a bullet from the specified alien.

        Args:
            alien (Turtle): Alien turtle.
        """
        bullet = Turtle(shape="square")
        bullet.shapesize(0.05, 0.8, 0)
        bullet.pencolor("white")
        bullet.penup()
        spark = self.create_spark(x=alien.xcor(), y=alien.ycor())
        self.sparks.append(spark)
        bullet.goto(x=alien.xcor(), y=alien.ycor())
        bullet.setheading(-90)
        bullet.forward(10)
        self.bullets.append(bullet)

    def move_bullets(self):
        """
        Move the bullets.
        """
        for bullet in self.bullets:
            bullet.forward(20)
