from turtle import Turtle

FONT = ("Courier", 8, "normal")


class Writer(Turtle):
    """ Writer class to stamp the user value on to the map"""

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def map_write(self, x_cor, y_cor, state_name):
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(state_name, align="center", font=FONT)