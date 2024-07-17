from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(arg=f"Score: {self.score}", align= ALLIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align= ALLIGNMENT, font= FONT)

    def score_incrementer(self):
        self.clear()
        self.score += 1
        self.score_update()
