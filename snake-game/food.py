from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.penup()
        self.color("blue")
        self.x_coord = 0
        self.y_coord = 0
        self.refresh()

    def refresh(self):
        self.x_coord = random.randint(-280, 280)
        self.y_coord = random.randint(-280, 280)
        self.goto(self.x_coord, self.y_coord)

    def get_coordinates(self):
        return self.x_coord, self.y_coord

