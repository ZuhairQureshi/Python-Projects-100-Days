import turtle
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

global screen

file = open("data.txt")
high_score = int(file.read())

def game():
    screen = Screen()
    screen.clear()
    playing = True
    score = 0
    game_screen = Screen()
    game_screen.setup(600, 600)
    game_screen.listen()
    game_screen.tracer(0)
    game_screen.bgcolor("black")
    score_turtle = Turtle()
    score_turtle.penup()
    score_turtle.hideturtle()
    style = ('Courier', 10)
    score_turtle.color("pink")

    my_snake = Snake()
    food = Food()

    game_screen.onkey(my_snake.face_up, "w")
    game_screen.onkey(my_snake.face_down, "s")
    game_screen.onkey(my_snake.face_right, "d")
    game_screen.onkey(my_snake.face_left, "a")

    while playing:

        time.sleep(0.1)
        game_screen.update()
        my_snake.move(game_screen)


        x_coord = my_snake.head.xcor()
        y_coord = my_snake.head.ycor()

        within_bounds = 285 >= x_coord >= -285 and 280 >= y_coord >= -280

        if not within_bounds:
            playing = False

        if my_snake.head.distance(food.get_coordinates()) <= 15:
            food.refresh()
            score += 1
            my_snake.new_segment()
            score_turtle.clear()

        for segment in my_snake.snake[1:]:
            if my_snake.head.distance(segment.pos()) <= 15:
                playing = False

        score_turtle.goto(-200, 280)
        score_turtle.write(f"Score: {score}", font=style, align="center")
        score_turtle.goto(200, 280)
        score_turtle.write(f"High score: {high_score}", font=style, align="center")

    replay(screen, score)


def replay(screen, score):
    global high_score

    if score > high_score:
        high_score = score
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    print(high_score)

    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.listen()
    prompt = Turtle()
    prompt.hideturtle()
    prompt.setpos(0,0)
    prompt.color("white")
    prompt.write("Press 'p' to play again or 'q' to exit", font = ("Courier", 15, "italic"), align = "center")
    screen.onkeypress(game, "p")
    screen.onkeypress(screen.bye, "q")
    screen.exitonclick()

game()
