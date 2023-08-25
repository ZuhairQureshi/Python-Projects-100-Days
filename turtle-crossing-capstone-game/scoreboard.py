from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over. Press 'p' to restart.", align="center", font=FONT)