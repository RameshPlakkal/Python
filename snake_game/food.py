from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.turtlesize(0.5, 0.5)
        self.speed("fastest")
        self.gen_food()

    def gen_food(self):
        x = random.randint(-210, 210)
        y = random.randint(-210, 210)
        self.goto(x, y)
