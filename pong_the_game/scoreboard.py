""" Defines the scoreboard and used for displaying player score"""

from turtle import Turtle

FONT = ('Felix Titling', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.player_1_score = 0
        self.player_2_score = 0
        self.penup()
        self.hideturtle()
        self.display_scoreboard()

    def player_1_track_score(self):
        self.player_1_score += 1

    def player_2_track_score(self):
        self.player_2_score += 1

    def display_scoreboard(self):
        self.clear()
        self.goto(-90, 230)
        self.write(f"{self.player_1_score}", align="center", font=FONT)
        self.goto(90, 230)
        self.write(f"{self.player_2_score}", align="center", font=FONT)