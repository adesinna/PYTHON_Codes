import datetime as dt
import random
import smtplib
import pandas as pd

# ----------------- Data -------------------------

# read the csv file
data = pd.read_csv('birthdays.csv')

# Change it to a list of dictionary, with each column being the key
birthday_data = data.to_dict(orient="records")


# ----------------Letter -----------------------------
NAME_HOLDER = "[NAME]"
# Read the 3 letters
with open("letter_templates/letter_1.txt") as letter_file:  # we open the letter file needed!
    letter_1 = letter_file.read()

with open("letter_templates/letter_2.txt") as letter_file:  # we open the letter file needed!
    letter_2 = letter_file.read()

with open("letter_templates/letter_3.txt") as letter_file:  # we open the letter file needed!
    letter_3 = letter_file.read()

# List the 3 letters
letter_list = [letter_1, letter_2, letter_3]

# Pick a random letter
random_letter = random.choice(letter_list)


# Let get the date
now = dt.datetime.now()  # shows you the present date and time
year = now.year
month = now.month
day = now.day

# Condition in sending letter
for dit in birthday_data:
    if dit['year'] == year and dit['month'] == month and dit['day'] == day:
        # Get the index of that dictionary in the list
        index = birthday_data.index(dit)
        current_dict = birthday_data[index]

        # Add the person name to letter
        new_letter = random_letter.replace(NAME_HOLDER, current_dict['name'])  # use the replace method

        # Write the new letter somewhere
        with open(f"letter_templates/letter_for_{current_dict['name']}.txt", mode='w') as complete_letter:
            complete_letter.write(new_letter)  # write new letter in each file

        # Read the saved file
        with open(f"letter_templates/letter_for_{current_dict['name']}.txt", mode='r') as complete_letter:
            letter = complete_letter.read()

        # Now send the letter
        my_email = 'shananatest@gmail.com'
        password = 'N4A5f#cRX*bR$'

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # We create a connection to smtp server
            connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
            connection.login(user=my_email, password=password)  # Login to your mail
            connection.sendmail(
                from_addr=my_email, to_addrs=current_dict['email'],
                msg=f'Subject:Hello\n\n{letter}'
            )

