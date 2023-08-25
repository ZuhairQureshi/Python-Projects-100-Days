import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"   # US map, within working directory
quit = False   # checks if user has quit
score = 0  # states guessed correctly

with open("high_score.txt") as file:
    high_score = int(file.read())

# Create the turtle that writes the state names onto the screen
state_name = turtle.Turtle()
state_name.speed(10)
state_name.hideturtle()
state_name.penup()
state_name.goto(300, 250)
state_name.write(f"High score: {high_score}")

# Make the US map into a turtle shape and display it
screen.addshape(image)
screen.setup(800, 600)
turtle.shape(image)


# Read the state name file and create dictionary for state name + coordinates pairing.
data = pd.read_csv("50_states.csv")
states_dict = {}

for i in range(data.shape[0]):
    state = data["state"][i]
    x = int(data["x"][i])
    y = int(data["y"][i])
    states_dict[state] = (x, y)


while score < 50 and not quit:
    answer = screen.textinput(title=f"{score}/50) correct", prompt="Guess a state name. Enter 'q' to quit: ")

    answer = answer[0].upper() + answer[1:]

    if answer == 'Q':
        quit = True

    elif answer in states_dict.keys():
        score += 1
        state_name.goto(states_dict[answer])
        state_name.write(answer, align="center", font=("Courier", 8, "normal"))


# Rearrange text to center
state_name.goto(0,0)

if not quit:
    state_name.clear()
    state_name.write("Congratulations. You named all 50 states. \nClick X to exit.", align = "center", font=("Courier", 20, "normal"))

else:
    state_name.write("Click X to exit.", align = "center", font=("Courier", 20, "normal"))

if score > high_score:
    with open("high_score.txt", mode = "w") as file:
        file.write(str(score))

turtle.mainloop()