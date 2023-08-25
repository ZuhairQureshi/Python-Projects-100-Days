import datetime as dt
import pandas as pd
import smtplib
import random

##################### Extra Hard Starting Project ######################

# Check if today matches a birthday in the birthdays.csv

my_user = "zuhair.qureshi5@gmail.com"
my_pass = "xarocztdkbojqrgn"

# Create the current time datetime object and create a birthday inventory
now = dt.datetime.now()
bday_info = pd.read_csv("birthdays.csv")

# Loop through the birthday entries
for (index, row) in bday_info.iterrows():

    # Check if today is a birthday for this entry
    if row.month == now.month and row.day == now.day:
        name = row["name"]

        # Open the letter template and replace the placeholder with the entry name
        with open("./letter_templates/letter_1.txt") as letter_file:
            letter = letter_file.read()
            revised_letter = letter.replace("[NAME]", name)

        # Connect to the appropriate smtp server with correct port
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()

            # Login and send the email with the letter as the contents
            connection.login(user=my_user, password=my_pass)
            connection.sendmail(
                from_addr=my_user,
                to_addrs=row.email,
                msg=f"Subject:Python Birthday Program\n\n{revised_letter}")






