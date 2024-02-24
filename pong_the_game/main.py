# TODO Define the screen and its elements within main.py
# TODO Define a class to initialize the game, create paddle with movements,
#       generate the ball and move
#       detect collision with wall and paddle
# TODO Define a class to capture the score and display on the screen
# TODO Define a class for exit logic
# TODO (Good to have) - provide multiplayer option.
#

from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import *
import time

paddle_coordinates = [(350, 0), (-350, 0)]

""" Define the Screen for the game."""
screen = Screen()
screen.title("Pong - The Game!")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

""" Create paddle and define the paddle movements"""

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
screen.listen()
screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")
screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")

score_board = Scoreboard()
ball = Ball()

""" Run the game """
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 350:
        ball.x_bounce()
        ball.up_ball_speed()
    # Detect collision with left paddle. Can be added to the above but kept separate for simplicity
    if ball.distance(left_paddle) < 60 and ball.xcor() < -350:
        ball.x_bounce()
        ball.up_ball_speed()

    # Detect paddle miss and update score
    if ball.xcor() > right_paddle.xcor():
        ball.reset_ball()
        score_board.player_1_track_score()
        score_board.display_scoreboard()
    if ball.xcor() < left_paddle.xcor():
        ball.reset_ball()
        score_board.player_2_track_score()
        score_board.display_scoreboard()


screen.mainloop()
