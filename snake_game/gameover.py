from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        # self.goto(0, 0)
        self.write("Game Over", False, ALIGNMENT, font=FONT)

    def game_over(self):
        pass
