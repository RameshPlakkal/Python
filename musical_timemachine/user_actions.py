from datetime import datetime, date
from tkinter.simpledialog import askstring
from tkinter import messagebox


class UserActions:

    def __int__(self):
        self.user_date_choice = date.today()

    def take_user_input(self):
        """Takes user input on the date to filter top musical titles"""
        user_date_choice = askstring(title="Musical TimeMachine 🎶",
                                     prompt="Which year do you want to travel? Type date in format \n"
                                            "YYYY-MM-DD")

        valid_date = self.validate_user_input(user_date_choice)
        if valid_date:
            return user_date_choice

    def validate_user_input(self, user_choice):
        try:
            date.fromisoformat(user_choice)
            self.user_date_choice = user_choice
            return True
        except ValueError:
            messagebox.showinfo(title="Musical TimeMachine 🎶", message="Date should be in format YYYY-MM-DD")
            self.take_user_input()
