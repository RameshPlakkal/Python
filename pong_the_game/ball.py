
""" Defines how the ball is created and the ball movements in different scenarios
 1. collision to wall
 2. collision to paddle
 """

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1, 1)
        self.x_move = 8
        self.y_move = 8

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_bounce()

    def up_ball_speed(self):
        self.speed(0)