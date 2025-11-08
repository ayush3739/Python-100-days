import requests
from datetime import datetime
import smtplib
import time

my_email="Ypur mail here"
passw="Yo8ur pass_key"
MY_LAT =  'Your latitude'
MY_LONG =  'Your longitude'

def check_position():
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and ( MY_LONG- 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False


def is_night():
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
    if  (time_now.hour >= sunset or time_now.hour <= sunrise):
        return True



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

    while True:
        time.sleep(60)
        if is_night()and check_position():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=passw)

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="reciever's mail",
                    msg="Subject: Iss position with the datetime\n\nlook up at the sky."
                    )



