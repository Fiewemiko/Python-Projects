import requests

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC03b8fbfcb269ad584ef39600c94bf7fd"
auth_token = "3409b73c8ac9b5373aa9add1474fdd4e"

client = Client(account_sid, auth_token)

ANGELA_API = "69f04e4613056b159c2761a9d9e664d2"
API_KEY = "d8fe9a1e9f380082a0e9b61477632642"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
London_Api = "https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=69f04e4613056b159c2761a9d9e664d2"

wheather_params = {
    'lat': 51.50,
    'lon': -0.127,
    'apiid': ANGELA_API
}

response = requests.get(url=London_Api)
print(response.json())
# error 401 when using owm ENDPOINT - need subscription on OpenWhether

weather_data = response.json()
wheather_main_situation = weather_data["weather"][0]['id']
print(wheather_main_situation)

if wheather_main_situation > 700:
    print("Bring an Umbrella")

message = client.messages \
    .create(
         from_='+1 478 888 6019',
         body='Wiktoria to malutki stolczyk ☔',
         to='+48724876158'
     )

print(message.body)
