import requests
from twilio.rest import Client


LAT = 42.882004
LON = 74.582748
API_KEY = "c6a673dafaaef334411f73a463a4031d"
parameter = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}
URL = "https://api.openweathermap.org/data/2.5/forecast"

ACC_SID = "__"
AUTH_TOKEN = "__"

response = requests.get(url=URL, params=parameter)
response.raise_for_status()
data = response.json()

print(data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(ACC_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Do not forget your umbrella!",
        from_ = "trial_num",
        to="phone_num")


print(message.status)
