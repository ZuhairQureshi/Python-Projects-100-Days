import random
from turtle import Turtle, Screen


turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_y_pos = 100
racing = False
guess = False

# Initialize the display screen
screen = Screen()
screen.setup(500, 400)

# Ask the user which colored turtle they think will win.
user_inp = screen.textinput(title = "Welcome to the turtle race!", prompt = "Which turtle do you think will "
                                                                            "win? (red/orange/yellow/green/blue/purple): ")

#Make sure user enters some input
if user_inp:
    racing = True

for i in range(6):
    turtles.append(Turtle(shape = "turtle"))
    turtles[i].color(colors[i])      # create 6 turtles: red, orange, yellow, green, blue, purple
    turtles[i].penup()               # we don't need to trace path in this program
    turtles[i].goto(-230, start_y_pos)  # align them all on the left side of the screen
    start_y_pos -= 50                # space them out by 50 units vertically

while racing:
    for i in range(6):
        turtles[i].forward(random.randint(5,15))  # turtles take random size steps

        if turtles[i].pos()[0] > 230:   # if a turtle reaches the right side of screen
            if colors[i] == user_inp:   #if the user chosen color is the winner
                print(f"You were right! {colors[i].upper()} won!")

            else:
                print(f"You were wrong. {colors[i].upper()} won...")

            racing = False  # end the program
            break

screen.bye()
