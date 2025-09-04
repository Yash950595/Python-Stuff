import requests
from datetime import datetime

application_id="8ca5cf00"
application_key="d8df2fcddc2933ddc95dbecc789130ab"

Gender="male"
weight=70
height=175
age=20

exercise_stats_url="https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_ques=input("What workout did you do today? \n")

headers={
    "x-app-id":application_id ,
    "x-app-key":application_key,
     "x-remote-user-id": "0"
}

exercise_parameters={
    "query":exercise_ques,
    "gender":Gender,
    "weight_kg":weight,
    "height_cm":height,
    "age":age
}

exercise_response=requests.post(url=exercise_stats_url,json=exercise_parameters,headers=headers)
result=exercise_response.json()

sheet_endpoint="https://api.sheety.co/ec1ebf99faefb7f0f1d842a3016fc952/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_headers = {
    "Authorization": "Bearer YOUR_SHEETY_TOKEN"
}

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

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=sheet_headers)

    print(sheet_response.text)