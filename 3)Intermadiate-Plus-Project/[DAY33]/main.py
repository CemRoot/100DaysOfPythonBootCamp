import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "YOUR MAIL"  # Your email address
MY_PASSWORD = "YOUR PASS"  # Your password
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude


def is_iss_overhead():
	"""
	Checks if ISS is overhead
	:return: #True if ISS is overhead, #False if not
	"""
	response = requests.get(url="http://api.open-notify.org/iss-now.json")  # ISS current position
	response.raise_for_status()  # If there is an error, it will raise an error
	data = response.json()  # Converts the response to a json object

	iss_latitude = float(data["iss_position"]["latitude"])  # Gets the latitude of the ISS
	iss_longitude = float(data["iss_position"]["longitude"])  # Gets the longitude of the ISS

	# Your position is within +5 or -5 degrees of the iss position.
	if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
		return True


def is_night():  #
	"""
	Checks if it is night
	:return:  #True if it is night, #False if not
	"""
	parameters = {
		"lat": MY_LAT,  # Your latitude
		"lng": MY_LONG,  # Your longitude
		"formatted": 0,  # Formats the response to a json object
	}
	response = requests.get("https://api.sunrise-sunset.org/json",
	                        params=parameters)  # Gets the sunrise and sunset times
	response.raise_for_status()  # If there is an error, it will raise an error
	data = response.json()  # Converts the response to a json object
	sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Gets the sunrise time
	sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # Gets the sunset time

	time_now = datetime.now().hour  # Gets the current time

	if time_now >= sunset or time_now <= sunrise:  # If it is night
		return True


while True:
	time.sleep(60)  # Waits for 60 seconds
	print("Checking...")
	if is_iss_overhead() and is_night():  # If ISS is overhead and it is night
		connection = smtplib.SMTP("smtp.gmail.com", 587)  # Sets up the connection to gmail server
		connection.starttls()  # Starts the TLS connection
		connection.login(MY_EMAIL, MY_PASSWORD)  # Logs in to gmail
		connection.sendmail(
			from_addr=MY_EMAIL,
			to_addrs=MY_EMAIL,
			msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."  # Sends a message to your email
		)
