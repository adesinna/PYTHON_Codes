# An Application Programming Interface is a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with external system!

# API Endpoint: It is the location where the data is (url of the api)
# API Request: To make a request

# 1XX means hold on
# 2XX means Successful
# 3XX means go away
# 4XX means you made a mistake
# 5XX means server screwed up

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response.status_code)  # It gives it a response code
response.raise_for_status()

# How to get our data
data = response.json()
print(data)
position = data['iss_position']
iss_position = (position['latitude'], position['longitude'])
print(iss_position)





