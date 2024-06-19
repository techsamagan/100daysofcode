import requests
from datetime import datetime

API_ID = "596fd171"
API_KEY = "51413b72fca51b74d8a216db63ecd8aa"
GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 185
AGE = 18
#
sheety_endpoint = "https://api.sheety.co/8770d1eda53a01f2846505862b8a3d48/myWorkouts/workouts"


#
headers = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell us, which exercises you did: \n>>")

exercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
print(today)

now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs ={
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers={"Authorization": "Bearer 123456789qwertyuioasdfghjklzxcvbnm"})

print(sheet_response.text)

