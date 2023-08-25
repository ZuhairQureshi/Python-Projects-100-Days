import turtle
from turtle import Turtle, Screen
import random

color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]
timmy = Turtle()
screen = Screen()

turtle.colormode(255)

"""
INSTRUCTIONS:
- painting must be 10 x 10 dots
- dots should have a radius of 20 and be spaced apart by 50 pixels from each other
"""
timmy.penup()
start_x = -300
start_y = -350
timmy.speed(20)
timmy.hideturtle()
screen.setup(800, 775)

for i in range(10):                     # 10 rows
    timmy.setpos(start_x, start_y)      # set the starting position for the given row

    for j in range(10):                 # each row has 10 dots
        timmy.pendown()
        color = random.choice(color_list)
        timmy.color(color, color) # set the pen color and the filling color, respectively

        #alternatively, we could use timmy.dot(size, color)
        timmy.begin_fill()
        timmy.circle(20)         # create the filled in shape (with this block of code)
        timmy.end_fill()


        timmy.penup()            # lift the pen while moving forward to draw the next circle
        timmy.forward(70)

    start_y += 70         # set the posn for a new row by moving vertically from the start point



screen.exitonclick()