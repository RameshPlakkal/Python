import turtle as t
import random

screen = t.Screen()
tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color


tim.speed(20)
tim.pensize(0)
for _ in range(int(360 / 5)):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

screen.mainloop()
