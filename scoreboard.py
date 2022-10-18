from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.update_score()

    def level_up(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.penup()
        self.goto(-280, 250)
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAMEOVER", align="center", font=FONT)
