from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.pensize(3)
timmy.speed(20)


# Define all movement functions
def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.back(10)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


#Define clear screen method to clear screen and reset turtle
def clear_screen():
    timmy.home()
    timmy.clear()


screen.listen()

# Key Press: W to move forward, S to move backward, D to rotate right, A to rotate left
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='a', fun=turn_left)

screen.onkeypress(key='c', fun=clear_screen)  # resets the drawing and drawer

screen.exitonclick() # leave pop-up
