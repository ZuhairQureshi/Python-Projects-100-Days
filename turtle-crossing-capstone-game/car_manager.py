from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-270, 270))
        car.shapesize(stretch_len=3, stretch_wid=1)
        self.cars.append(car)

    def move(self):
        """Moves the cars"""
        for i in range(len(self.cars)):
            car = self.cars[i]
            car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def clear_list(self):
        for i in range(len(self.cars)):
            self.cars[i].clear()
            self.cars[i].hideturtle()
