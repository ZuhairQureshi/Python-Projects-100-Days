
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()         # only want to see text, not turtle
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    # Displaying the updated scores for each player
    def update(self):
        self.clear()
        self.goto(200, 190)
        self.write(self.r_score, align = "center", font = ("Courier", 80, "normal"))
        self.goto(-200, 190)
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))

    # Display when one of the players wins
    def declare_winner(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(f"{winner} wins. Press 'r' to restart.", align="center", font=("Courier", 20, "normal"))

    # Updating the scores
    def l_point(self):
        self.l_score += 1

        if self.l_score < 10:
            self.update()
        else:
            self.declare_winner("Left")

    def r_point(self):
        self.r_score += 1

        if self.r_score < 10:
            self.update()
        else:
            self.declare_winner("Right")

    def reset_scores(self):
        self.l_score = 0
        self.r_score = 0
        self.update()
