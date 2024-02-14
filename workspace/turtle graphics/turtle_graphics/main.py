import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

turtle_colors = ["red", "blue", "green", "black", "yellow", "magenta", "purple", "orange", "grey"]
turtle_in_race = []
race_turtles = int(t.textinput("Turtle Race 🐢", "Input how many turtles to race :"))

for count in range(race_turtles):
    tim = t.Turtle("turtle")
    tim.penup()
    tim.color(turtle_colors[count])
    tim.goto(-230, -150 + count * 50)
    turtle_in_race.append(tim)

user_selection = t.textinput("Turtle Race 🐢", "Which turtle will win? Enter the turtle color :").lower()

start_race = t.textinput("Turtle Race 🐢", "Start Race? Yes / No").lower()
winner = ""
RACE_ON = True

if start_race:
    while RACE_ON:

        for turtle in turtle_in_race:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > 250:
                winner = turtle.getturtle()
                RACE_ON = False

if winner.pencolor() == user_selection:
    print(f"Your turtle {winner.pencolor()} has won the race!")
else:
    print(f"You lose! {winner.pencolor()} wins the race")

screen.mainloop()
