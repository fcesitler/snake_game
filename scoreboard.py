from food import Food
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)



