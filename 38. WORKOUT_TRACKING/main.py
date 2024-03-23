import requests
from datetime import datetime
import os

#go to this url to see google sheet
# https://docs.google.com/spreadsheets/d/1mmtQhGHUYlWLGAqRDOPY5vFYFm9GNx3oqaUQGHBFUiU/edit#gid=0

APP_ID="9b35aa49"
API_KEY="a645ad9b5feb2d6ea521f7d05dffb9d5"
TOKEN=os.environ["TOKEN"]
SHEET_ENDPOINT='https://api.sheety.co/09a3879d46b42df5119ef6f9eb995088/workoutTracking/workouts'
EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER="female"
WEIGHT_KG=49
HEIGHT_CM=160
AGE=21

now = datetime.now()
date_today = now.date().strftime("%d/%m/%Y")
time_now = now.time().strftime("%X")

exercise_text = input("Tell me which exercise u did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
person_info = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE,
}
response=requests.post(EXERCISE_ENDPOINT, headers=headers, json=person_info)
response.raise_for_status()
json_response=response.json()
exercises=json_response["exercises"]

for exercise in exercises:

    sheet_inputs={
        "workout":{
            "date":date_today,
            "time":time_now,
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories'],
            "exercise":exercise["user_input"].title(),
        }
    }
    sheety_headers = {
        "Authorization": f"Basic {os.environ['TOKEN']}"
    }
    sheety_response=requests.post(SHEET_ENDPOINT,
                                  json=sheet_inputs,
                                  headers=sheety_headers
                                  )
    sheety_response.raise_for_status()
    print(sheety_response.text)

