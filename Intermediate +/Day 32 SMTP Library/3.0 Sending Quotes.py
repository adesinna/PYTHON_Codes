import datetime as dt
import random
import smtplib

my_email = 'shananatest@gmail.com'
password = 'N4A5f#cRX*bR$'


with open('quotes.txt') as motivation:  # we open up the file folder!
    quotes = motivation.readlines()  # readline is different from read, read lines() will list the content of the list

random_quote = random.choice(quotes)


stripped_quote = random_quote.strip()  # to remove the \n from the names
print(stripped_quote)


now = dt.datetime.now()

day = now.weekday()


if day == 1:
    with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:  # We create a connection to smtp server (Simple Mail Transfer
        # Protocol)
        connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
        connection.login(user=my_email, password=password)  # Login to your mail
        connection.sendmail(
            from_addr=my_email, to_addrs='shananatest@yahoo.com',
            msg=f'Subject:Motivational Quote\n\n{stripped_quote}'
        )
