import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
def CheckISSPos():
    if abs(iss_longitude - MY_LONG) =< 5 and abs(iss_latitude - MY_LAT) =< 5:
        CheckIfDark()
    else:
# and it is currently dark
def CheckIfDark():
    if time_now >= sunset or timenow <= sunrise:
        SendEmail:
# Then send me an email to tell me to look up.
def SendEmail:
    print("iss is overhead")
    sleep(60)
    SendEmail()
# BONUS: run the code every 60 seconds.
SendEmail()


