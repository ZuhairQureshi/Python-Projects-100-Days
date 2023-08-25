from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)   # paddle is 20 x 100
        self.color("white")
        self.speed(10)
        self.penup()
        self.goto(position)

    # Functions to move up or down within the screen boundaries (by 20 units)
    def move_up(self):
        if self.ycor() < 245:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)

