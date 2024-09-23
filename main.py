import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "ENTER YOUR EMAIL HERE"
MY_PASSWORD = "ENTER YOUR PASSWORD HERE"
MY_LAT = 41.608635  # enter your latitude
MY_LNG = 21.745275  # enter your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # iss_position = (longitude, latitude)

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        from_addr = MY_EMAIL
        to_addr = MY_EMAIL
        msg = "Subject:Look Up☝️\n\nThe ISS is above you in the sky.🌌🙂"
