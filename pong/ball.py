import math
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.pace = 25     # how fast ball will move
        self.start_heading = 45  # starting direction of round: upper right
        self.setheading(self.start_heading)

    # Keep the ball moving at its current pace in its specific direction
    def move(self):
        self.forward(self.pace)

    # Reverse the ball's vertical movement upon hitting the ceiling or floor
    def y_bounce(self):
        self.setheading(-self.heading())

    # Reverse the ball's horizontal movement upon hitting a paddle
    def x_bounce(self):
        self.setheading(180 - self.heading())
        self.pace += 2   # make the ball move faster with each hit

    # Reset default values for when ball goes out of bounds
    def reset(self):
        self.goto(0,0)
        self.x_bounce()
        self.pace = 25

