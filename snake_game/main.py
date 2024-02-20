""" The world-famous snake game.
This is what you would have played on the Nokia 3XXX series
Creator @ Ramesh Plakkal
ver 1.0
"""
from turtle import Screen
import time

from gameover import GameOver
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.listen()
screen.tracer(0)

anime_snake = Snake("brown")
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(anime_snake.up, "Up")
screen.onkeypress(anime_snake.down, "Down")
screen.onkeypress(anime_snake.left, "Left")
screen.onkeypress(anime_snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    anime_snake.move()

    # Detect collision with food :)
    if anime_snake.head.distance(food) < 15:
        score_board.gen_score()
        food.gen_food()
        anime_snake.append_snake()
    # Detect collision with wall
    if anime_snake.head.xcor() >= 250 or anime_snake.head.xcor() <= -250 or anime_snake.head.ycor() >= 250 or anime_snake.head.ycor() <= -250:
        game_on = False
        game_over = GameOver()

    # Detect collision with any snake body part
    for snake in anime_snake.snake_body[1:]:
        if anime_snake.head.distance(snake) < 10:
            game_on = False
            game_over = GameOver()


screen.mainloop()
