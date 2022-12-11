from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Frogger(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)
