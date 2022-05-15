import requests
import smtplib
import os

LAT = 7.418090
LNG = 3.905210
KEY = 'bfeebb1022b47f04535d5dd54994ca23'


parameters = {
    'lat': LAT,
    'lon': LNG,
    'appid': KEY,
    'exclude': 'current,minutely,daily'

}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
sliced_data = weather_data['hourly'][0:12]  # get the first 12 hours

will_rain = False

for hour_data in sliced_data:
    condition_code = hour_data['weather'][0]['id']  # getting the code for rain

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # Now send the letter
    my_email = 'shananatest@gmail.com'
    password = 'N4A5f#cRX*bR$'

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # We create a connection to smtp server
        connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
        connection.login(user=my_email, password=password)  # Login to your mail
        connection.sendmail(
            from_addr=my_email, to_addrs='aladesaea@gmail.com',
            msg=f'Subject:Rain Update!\n\nBring Out Your Umbrella, It will rain today!. Also big daddy loves you'
        )
else:
    # Now send the letter
    my_email = 'shananatest@gmail.com'
    password = 'N4A5f#cRX*bR$'

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # We create a connection to smtp server
        connection.starttls()  # Next we secure connection to the server through tls (Transport Layer Security)
        connection.login(user=my_email, password=password)  # Login to your mail
        connection.sendmail(
            from_addr=my_email, to_addrs='aladesaea@gmail.com',
            msg=f'Subject:Rain Update!\n\nNo Rain today. Big Papi loves you!'
        )






