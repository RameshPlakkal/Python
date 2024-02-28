import turtle
from turtle import Screen
import pandas
from map_write import Writer

FONT = ("Verdana", 8, "normal")
TITLE = "Guess the State "
PROMPT = "What's another state name?"
COUNT = 0

# Set up the screen

screen = Screen()
screen.title("Quiz - Indian States.")
image = "giphy.gif"
screen.addshape(image)
turtle.shape(image)


# ======================== Code to get the state coordinates =========================
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# =====================================================================================

write = Writer()

# Read the csv
core_data = pandas.read_csv("indian_states.csv")

# Loop this all states answered
game_on = True
while game_on:
    user_input = turtle.textinput(f"{TITLE} {COUNT}/26 ", PROMPT).title()
    state_data = core_data[core_data.state == user_input]
    if state_data.empty:
        pass
    else:
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        write.map_write(x_cor, y_cor, user_input)

        COUNT += 1
        if COUNT == 26:
            write.map_write(215, 226, "Well Done!")
            game_on = False

screen.mainloop()
