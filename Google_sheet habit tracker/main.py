import requests
from datetime import datetime
import os


APP_ID = "5dec427f"
APP_key = "8489f9de897240e359d950d7bc4bd345"
SHEETY_API = "a29ee7510abd1412bdee5ec1c90d5805"
Nutronix_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
excerisie_input = input("Which exercise you did?: ")
sheety_ENDPOINT = "https://api.sheety.co/a29ee7510abd1412bdee5ec1c90d5805/myWorkouts/workouts"


NUTRONIX_HEADER = {
    "x-app-id":APP_ID,
    "x-app-key":APP_key,
    "x-remote-user-id":"0"
}

nutronix_params ={
    'query': excerisie_input,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 184 ,
    "age": 23
}

nut_response = requests.post(url=Nutronix_ENDPOINT,headers=NUTRONIX_HEADER,json=nutronix_params)
print(nut_response.text)


excersises_number = len(nut_response.json()['exercises'])

auth = ("filipniewczas","haslohaslo")

for _ in range(excersises_number):
    sheety_params ={
        'workout':{
        "date":datetime.now().strftime("%d/%m/%Y"),
        "time":datetime.now().strftime("%H:%M:%S"),
        "exercise":nut_response.json()['exercises'][_]['user_input'],
        "duration":nut_response.json()['exercises'][_]['duration_min'],
        "calories":nut_response.json()['exercises'][_]['nf_calories']}
    }
    sheety_response = requests.post(url=sheety_ENDPOINT,json=sheety_params,auth=auth)

