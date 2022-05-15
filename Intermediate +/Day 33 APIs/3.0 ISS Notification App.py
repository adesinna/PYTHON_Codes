import requests
from datetime import datetime
import smtplib
import time

# ------------------ Getting Our Time and Location --------------------
LAT = 6.524379
LNG = 3.379206
parameters = {
    'lat': LAT,
    'lng': LNG,
    'formatted': 0,

}

response_location = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response_location.raise_for_status()
data_location = response_location.json()
sunrise = data_location['results']['sunrise']
sunset = data_location['results']['sunset']

# Separate the T
first_sep_sr = sunrise.split('T')

# Take the time part and separate the +
second_sep_sr = first_sep_sr[1].split('+')

# Now we can take out the hour and minutes
third_sep_sr = second_sep_sr[0].split(":")

sunrise_hour = third_sep_sr[0]
sunrise_minute = third_sep_sr[1]

print(f'Sunrise is {sunrise_hour}:{sunrise_minute}')

# Next we do it for sunset

# Separate the T
first_sep_ss = sunset.split('T')

# Take the time part and separate the +
second_sep_ss = first_sep_ss[1].split('+')

# Now we can take out the hour and minutes
third_sep_ss = second_sep_ss[0].split(":")

sunset_hour = third_sep_ss[0]
sunset_minute = third_sep_ss[1]

print(f'Sunrise is {sunset_hour}:{sunset_minute}')

time_now = datetime.now()
print(f'The present time is {time_now.hour}:{time_now.minute}')


# ----------------------Getting ISS Location  -----------------------
# Request for data from the end point
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
data_iss = response_iss.json()
iss_lat = float(data_iss["iss_position"]["latitude"])
iss_lng = float(data_iss["iss_position"]["longitude"])


# ==================== Condition and sending of mail ===================
while True:
    time.sleep(60)  # This allows the program to run every 60sec

    if time_now.hour > int(sunset_hour) and abs(iss_lat - LAT) <= 5 and abs(iss_lng - LNG) <= 5:
        my_email = 'shananatest@gmail.com'
        password = 'N4A5f#cRX*bR$'

        with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:  # We create a connection to smtp server
            connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
            connection.login(user=my_email, password=password)  # Login to your mail
            connection.sendmail(
                from_addr=my_email, to_addrs='aladesaea@gmail.com',
                msg=f'Subject:ISS Notification\n\nHello Bro, Shoot for the stars but do not shoot down ISS'
            )
        print('Go check mail')
