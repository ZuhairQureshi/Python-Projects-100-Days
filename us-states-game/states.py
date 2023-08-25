from turtle import Turtle


class States(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(10)
        self.penup()
        self.hideturtle()

    def assign_name(self, coordinates):
        self.goto(coordinates)

