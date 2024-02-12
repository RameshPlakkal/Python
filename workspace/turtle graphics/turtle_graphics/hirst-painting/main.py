import colorgram as cg
import turtle as t
import random

screen = t.Screen()
tim = t.Turtle()
extracted_colors = cg.extract("download.jpg", 50)
rgb_list = []


def get_rgb_list():
    for count in range(len(extracted_colors)):
        r = extracted_colors[count].rgb.r
        g = extracted_colors[count].rgb.g
        b = extracted_colors[count].rgb.b
        color_tuple = (r, g, b)
        rgb_list.append(color_tuple)
    return rgb_list


screen.colormode(255)
tim.penup()
tim.hideturtle()

tim.setpos(-10, 0)
for run_1 in range(10, 200, 15):
    for run_2 in range(10):
        tim.dot(10, random.choice(get_rgb_list()))
        tim.forward(20)
    tim.teleport(-10, run_1+5)



# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         tim.color(c)
#         tim.forward(steps)
#         tim.right(30)


screen.mainloop()
