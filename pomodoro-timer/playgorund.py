
for num in range(60, 65, -1):
    print(num)

# Logic before exploring canvas.after
#
#     for sec in range(60, 0):
#         print(sec)
#         time.sleep(1)
#         # canvas.delete("timer")
#         # canvas.create_text(300, 270, justify="center", text=f"{MINUTE}:{sec}", font=FONT, fill="white",
#         #                    tags="timer")
#         if sec < 10:
#             sec = f"0{sec}"
#
#         canvas.itemconfig("timer", text=f"{MINUTE}:{sec}")
#         canvas.update()
#
#         if RESET:
#             break
#
#         if sec == 0:
#             MINUTE -= 1
#             start_countdown()
#
#         if MINUTE == 0:
#             pomodoro_break()
