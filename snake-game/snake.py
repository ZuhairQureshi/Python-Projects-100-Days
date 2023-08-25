import time
from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.snake = []
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.generate_snake()
        self.directions = []
        self.head = self.snake[0]
        self.tail = self.snake[-1]
        self.collision = False

    def generate_snake(self):
        for i in range(3):
            self.snake.append(Turtle(shape="square"))
            self.snake[i].penup()
            self.snake[i].color("white")
            self.snake[i].goto(self.positions[i])

    def face_up(self):
        if int(self.head.heading()) != 270 and int(self.head.heading()) != 90:
            self.head.setheading(90)
        return

    def face_down(self):
        if int(self.head.heading()) != 270 and int(self.head.heading()) != 90:
            self.head.setheading(-90)
        return

    def face_right(self):
        if int(self.head.heading()) != 180 and int(self.head.heading()) != 0:
            self.head.setheading(0)
        return

    def face_left(self):
        if int(self.head.heading()) != 180 and int(self.head.heading()) != 0:
            self.head.setheading(180)
        return

    def new_segment(self):
        segment = Turtle(shape="square")
        segment.speed(10)
        segment.penup()
        segment.goto(self.snake[-1].pos())
        segment.color("white")
        self.snake.append(segment)

    def move(self, screen):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)

        print(self.positions)
        self.head.forward(20)



