import math
from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#ffcad4"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    start_button.configure(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        canvas.itemconfigure(tagOrId="break_type", text="Break!")
        start_countdown(long_break_sec)

    elif reps % 2 == 0:
        canvas.itemconfigure(tagOrId="break_type", text="Break!")
        start_countdown(short_break_sec)
    else:
        canvas.itemconfigure(tagOrId="break_type", text="Focus Time!")
        start_countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfigure(tagOrId="timer", text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, start_countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔️"
        check_marks.config(text=marks)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(tagOrId="break_type", text="Timer")
    check_marks.config(text="")
    canvas.itemconfigure(tagOrId="timer", text="00:00")
    start_button.configure(state="active", font=B_FONT, bg=GREEN)
    global reps
    reps = 0


# ---------------------------- UI SETUP ------------------------------- #
FONT = ("courier", 25, "bold")
B_FONT = ("Times New Roman", 8, "bold")
window = Tk()
window.title("Pomodoro")
window.config(background=YELLOW)
window.minsize(600, 500)

canvas = Canvas(height=400, width=400, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png", width=200, height=250)
canvas.create_image(300, 250, image=tomato_img)

canvas.create_text(300, 250, text="00:00", font=FONT, fill="white", tags="timer")
canvas.create_text(300, 100, text="Timer", font=FONT, fill=RED, tags="break_type")
canvas.grid_anchor("center")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=B_FONT, bg=GREEN, command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", font=B_FONT, bg=GREEN, command=reset_timer)
reset_button.grid(row=3, column=2)

check_marks = Label(fg=RED, bg=YELLOW, font=FONT)
check_marks.grid(row=4, column=3)

window.mainloop()
