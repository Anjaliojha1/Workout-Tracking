import requests
from datetime import datetime
# using nutritionix api

GENDER = "Female"
WEIGHT_KG = "75"
HEIGHT_CM = "160"
AGE = "22"

APP_ID = "2a0cf956"
APP_KEY = "502ed334074b63ae3efd7f20eed55652"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")




params = {
    "query":exercise_text ,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

header = {
    "Content-Type" : "application/json",
    "x-app-id": APP_ID,
    "x-app-key" :APP_KEY
}
response = requests.post(url=ENDPOINT, json=params, headers= header)
result = response.json()



sheety_url = "https://api.sheety.co/0f35d1a13b082d9c777efb7dd814f854/copyOfMyWorkouts/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs)


    print(sheet_response.text)




