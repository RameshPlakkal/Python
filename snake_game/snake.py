from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ This is a setup class to define the snake, its moves and all attributes"""

    def __init__(self, color):
        self.color = color
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    """The below 2 functions initialize the snake in hte first instance and also help with extending the snake length"""

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.fillcolor(self.color)
        snake.turtlesize(0.8, 0.8)
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    """ This function increases the snake length post hitting the food object"""

    def append_snake(self):
        # current_snake_length = len(self.snake_body)
        self.add_segment(self.snake_body[- 1].position())

    """ The below functions define the snake movement """

    def move(self):
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
