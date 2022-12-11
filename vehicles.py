from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "orange", "purple", "yellow", "black", "cyan", "indigo"]
STARTING_X = 300
STARTING_MOVE = 5
MOVE_INCREMENT = 10


class Vehicle:

    def __init__(self):
        self.garage = []
        self.speed = STARTING_MOVE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.up()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(STARTING_X, random_y)
            self.garage.append(new_car)

    def move_car(self):
        for car in self.garage:
            car.backward(STARTING_MOVE)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
