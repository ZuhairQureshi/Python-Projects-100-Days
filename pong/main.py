import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# restart the game after clicking 'p'
def restart():
    ball.reset()
    scoreboard.reset_scores()
    game()


# Create the screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  # turn off animations

# define the paddles and their locations
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))


# Create the ball and scoreboard
ball = Ball()
scoreboard = Scoreboard()

# Create the screen events (keyboard input)
screen.listen()
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")
screen.onkeypress(restart, "r")


# Game loop
def game():

    gaming = True

    while gaming:
        time.sleep(0.1)      # always delay each frame by 0.1 seconds

        # if the ball touches an upper boundary
        if ball.ycor() > 265 or ball.ycor() < -270:
            ball.y_bounce()

        # if the ball touches a paddle and is facing the right direction and in the right area
        if (320 < ball.xcor() < 350 and (0 < ball.heading() < 90 or 270 < ball.heading() < 360) and ball.distance(paddle1) <= 50) or (
                -320 > ball.xcor() > -350 and 90 < ball.heading() < 270 and ball.distance(paddle2) <= 50):
            ball.x_bounce()

        # if the ball goes out of bounds on the right
        elif ball.xcor() > 400:
            ball.reset()
            scoreboard.l_point()

        # if the ball goes out of bounds on the left
        elif ball.xcor() < -400:
            ball.reset()
            scoreboard.r_point()

        # if either of the players reaches 10, declare them the winner.
        if scoreboard.l_score == 10:
            gaming = False
            scoreboard.declare_winner("Left")

        elif scoreboard.r_score == 10:
            gaming = False
            scoreboard.declare_winner("Right")

        # Keep the ball moving and always update the screen frames
        ball.move()
        screen.update()


# call on the game loop
game()
screen.exitonclick()
