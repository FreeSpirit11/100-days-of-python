from turtle import Turtle

class Bunker:
    def __init__(self):
        """
        Initialize the Bunker object.

        This method sets up the Bunker attributes, such as the segments list,
        and calls the create_bunker method to generate the bunker segments.
        """
        self.segments = []
        self.create_bunker()

    def add_segement(self, i, j):
        """
        Add a bunker segment to the bunker.

        This method creates and adds a bunker segment (spike) to the bunker
        at the specified position (i, j).

        Parameters:
        - i (int): The x-coordinate of the bunker segment.
        - j (int): The y-coordinate of the bunker segment.
        """
        spike = Turtle()
        spike.shape("square")
        spike.color("springgreen")
        spike.shapesize(stretch_wid=1, stretch_len=0.01, outline=0)
        spike.penup()
        spike.goto(-410 + i, -80 - j)
        self.segments.append(spike)

    def create_bunker(self):
        """
        Create the bunker by adding bunker segments.

        This method generates the bunker structure by adding multiple bunker
        segments using the add_segement method.
        """
        k = 0
        for bunker in range(4):
            j = 0
            k += 140
            for row in range(5):
                i = k
                j += 22
                for column in range(40):
                    self.add_segement(i, j)
                    i += 3
