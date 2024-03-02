from tkinter import *

FONT = ("Ariel", 10, "bold")


def convert_2_km():
    # print(text_box.get())
    mile = float(text_box.get())
    result = round(mile * 1.60934, 2)
    answer.config(text=f"{result}  Km")


window = Tk()
window.minsize(height=150, width=350)
window.title("Converter - Miles to Kilometer.")
window.config(padx=20, pady=40)

miles = Label(text="Miles : ", pady=20, padx=20)
miles.grid(column=0, row=0)

text_box = Entry(width=10, background="light yellow", font=FONT)
text_box.focus()
text_box.grid(column=1, row=0)

equals = Label(text=" = ")
equals.grid(column=2, row=0)

answer = Label(text="0   Km", font=FONT)
answer.grid(column=3, row=0)

convert = Button(text="Convert", font=FONT, command=convert_2_km)
convert.grid(column=0, row=4)

window.mainloop()
