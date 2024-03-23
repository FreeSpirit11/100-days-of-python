from turtle import Turtle

class Shooter():
    def __init__(self):
        """
        Initialize the Shooter object.

        This method creates a shooter and helper shooters, initializing their
        attributes such as lasers and positions.
        """
        self.lasers = []
        self.shooters = []
        self.create_shooter(0, -260)
        self.create_helper_shooters()

    def create_shooter(self, i, j):
        """
        Create a main shooter.

        Args:
        - i: x-coordinate of the shooter
        - j: y-coordinate of the shooter

        This method creates a main shooter Turtle with specific attributes
        such as shape, size, color, and position. The shooter is appended to
        the list of shooters.
        """
        shooter1 = Turtle(shape="square")
        shooter1.shapesize(0.4, 3, 0)
        shooter1.color("springgreen")
        shooter1.penup()
        shooter1.goto(i, j)
        self.shooters.append(shooter1)

    def move_right(self):
        """
        Move the main shooter to the right.

        This method moves the main shooter forward by 20 units.
        """
        shooter1 = self.shooters[0]
        shooter1.forward(20)

    def move_left(self):
        """
        Move the main shooter to the left.

        This method moves the main shooter backward by 20 units.
        """
        shooter1 = self.shooters[0]
        shooter1.backward(20)

    def create_laser(self):
        """
        Create a laser for the main shooter.

        This method creates a laser Turtle for the main shooter, initializing
        its shape, size, color, and position. The laser is appended to the list
        of lasers.
        """
        shooter1 = self.shooters[0]
        laser = Turtle("square")
        laser.shapesize(0.1, 1)
        laser.color("springgreen")
        laser.penup()
        laser.goto(shooter1.xcor(), shooter1.ycor() + 20)
        laser.setheading(90)
        self.lasers.append(laser)

    def shoot(self):
        """
        Move all lasers forward.

        This method moves all lasers in the list forward by 10 units.
        """
        for laser in self.lasers:
            laser.forward(30)

    def create_helper_shooters(self):
        """
        Create helper shooters.

        This method creates helper shooters on specific positions
        and appends them to the list of shooters.
        """
        self.create_shooter(-260, -310)
        self.create_shooter(-180, -310)

    def get_helper_shooter(self):
        """
        Move the helper shooter to a main shooter position.

        This method moves the helper shooter to a main shooter position,
        making it act as a main shooter.
        """
        shooter1 = self.shooters[0]
        shooter1.goto(0, -260)
