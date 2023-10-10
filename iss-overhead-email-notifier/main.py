# Required imports
import requests
import time
import smtplib
from datetime import datetime

# SMTP login information
my_user = "zuhair.qureshi5@gmail.com"
my_pass = "abcdefghijkl"   # purposely edited for security purposes

# Checks if ISS is overhead
def iss_within_range():
    return abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5


def dark_outside():
    return time_now >= sunset or time_now <= sunrise


# Establish SMTP connection using credentials
def send_email(message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()

        connection.login(user=my_user, password=my_pass)
        connection.sendmail(
            from_addr=my_user,
            to_addrs="zuhair.q01@gmail.com",
            msg=f"Subject:ISS is overhead.\n\n{message}"
        )


# Define latitude and longitude for Toronto, Canada
MY_LAT = 43.651890
MY_LONG = -79.381706

# Collect information on coordinates directly below ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

# Define ISS coordinates
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Required parameters lat and long and optional parameter "formatted" to pass into .get() method
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Get information from sunrise sunset API
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Check if ISS is overhead
while True:

    # Sunrise and sunset timing collected to determine ISS visibility
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.utcnow().hour

    if iss_within_range() and not dark_outside():
        send_email("The ISS is directly above Toronto right now.")

    if iss_within_range() and dark_outside():
        send_email("The ISS is overhead in Toronto and it's dark outside. Look up, you might see it.")

    time.sleep(180)   # run a check every 3 minutes



