from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 21, "bold")
GAME_OVER_FONT = ("Courier", 27, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", font=GAME_OVER_FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()
