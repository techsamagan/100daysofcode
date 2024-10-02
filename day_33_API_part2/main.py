import requests
import datetime as dt
import smtplib
import time


MY_LAT = 51.507351
MY_LON = -0.127758
MY_EMAIL = "samnurd2005@gmail.com"
PASSWORD = "************"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lon = data["iss_position"]["longitude"]
    iss_lat = data["iss_position"]["latitude"]

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LON - 5 <= iss_lon <= MY_LON + 5:
        return True
    



def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LON,
        "formatted": 0,
    }
    response = requests.get( url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.starttls()
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="techsamagan@gmail.com", msg="It is close\n\nSee them it is close to you.")
