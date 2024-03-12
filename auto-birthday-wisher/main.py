import datetime as dt
import random
import smtplib
import pandas as pd
import os

# ---------------- Constants ---------------------------------- #
MY_EMAIL = "ramesh.plakkal@gmail.com"
APP_PASSWORD = "ludolplzrborsrqr"
HOST = "smtp.gmail.com"
SUBJECT = "Happy Birthday"
TODAY = dt.datetime.now()

# Read csv
data_file = pd.read_csv("birthdays.csv")
data_dict = data_file.to_dict(orient="records")

# Identify people with Birthday falling today
birthday_dict = {row["name"]: row.email for (index, row) in data_file.iterrows()
                 if TODAY.day == row.day and TODAY.month == row.month}
birthday_name = [key for key in birthday_dict]

# Prepare the Birthday message
any_template = random.choice(
    os.listdir("C:\\Ramesh\\Python\\workspace\\auto-birthday-wisher\\letter_templates"))

print(any_template)

b_name = 0
for name in birthday_name:
    with open(f"letter_templates/{any_template}") as letter:
        content = letter.read().encode()
        new_message = content.replace("[NAME]", name)

    # Send email
    with smtplib.SMTP(HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_dict[birthday_name[b_name]],
                            msg=f"Subject:{SUBJECT}\n\n {new_message}")

    b_name += 1
