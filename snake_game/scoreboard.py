from turtle import Turtle

ALIGNMENT = "right"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(220, 230)
        self.score = 0
        self.write(f"Score :  {self.score} ", False, ALIGNMENT, font=FONT)

    def gen_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score :  {self.score} ", False, ALIGNMENT, font=FONT)
