""" Defines the paddle and paddle movements."""

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.paddle_tracker = []
        self.create_paddles(coordinates)

    def create_paddles(self, coordinates):  # this can go into constructor
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def move_up(self):
        original_x = self.xcor()
        original_y = self.ycor()
        self.goto(original_x, original_y + 20)

    def move_down(self):
        original_x = self.xcor()
        original_y = self.ycor()
        self.goto(original_x, original_y - 20)
