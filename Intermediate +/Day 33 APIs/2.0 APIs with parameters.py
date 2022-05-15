# There are some APIs that require parameters
# Good examples is  https://api.sunrise-sunset.org/json API end point

import requests
from datetime import datetime

LAT = 6.524379
LNG = 3.379206
parameters = {
    'lat': LAT,
    'lng': LNG,
    'formatted': 0,
    
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

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
