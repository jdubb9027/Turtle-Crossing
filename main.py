from turtle import Screen
from frogger import Frogger
from scoring import Score
from vehicles import Vehicle
import time

DELAY = 0.1

# Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.title("Cross The Road")

# Screen animation
screen.tracer(0)

# Create turtle
player = Frogger()

# Initialize obstacles
vehicle = Vehicle()

# Initialize Scoring
score = Score()

# Move Player
screen.listen()
screen.onkeypress(key='Up', fun=player.move_up)

# Game over
game_on = True

while game_on:
    # Screen animation update
    screen.update()

    # Program speed control
    time.sleep(DELAY)

    # Create obstacles
    vehicle.create_car()
    vehicle.move_car()

    # Detect collision with north wall
    if player.ycor() > 300:
        player.goto(0, -280)
        vehicle.increase_speed()
        score.increase_level()
        score.update_level()

    # Detect collision with a vehicle
    for car in vehicle.garage:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False

screen.exitonclick()
