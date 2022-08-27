import requests
import pandas
from twilio.rest import Client
from tkinter import *

# ------KEYS - -----
api_key = "19d82a696bdc9da314ee50ef26381fc1"
MY_LONGITUDE = "36.896893"
MY_LATITUDE = "30.713324"

account_sid = "AC7c8da98f44aeb2731e7d795165b02c37"
auth_token = "0440747366124d530b1208b796f18ce2"
client = Client(account_sid, auth_token)
########################################
parameters = {
	"lat": MY_LATITUDE,
	"lon": MY_LONGITUDE,
	"appid": api_key,
	"exclude": "current,minutely,daily",
	"lang": "tr",
}
#test

def emergency():

	message = client.messages.create(
	from_='whatsapp:+14155238886',
	body='Bring an Umbrella',
	to='whatsapp:+380661508739'
)
	print(message.sid)
# ** ** ** ** ** *GUI ** ** ** ** ** *>
window = Tk()
window.title("SOS")

window.configure(pady=10, padx=10, background="white")

canvas = Canvas(width=10, height=10)
background_img = PhotoImage(file="sos.png")

kanye_img = PhotoImage(file="sos.png")
kanye_button = Button(height=100, width=100, image=kanye_img, highlightthickness=0, command=emergency)
kanye_button.grid(row=1, column=0)

window.mainloop()

# ** ** ** ** ** *MAIN ** ** ** ** ** *
# res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# res.raise_for_status()
# data_weather = res.json()
#
# data_hourly = data_weather["hourly"][:12]
# data_hourly_codes = [hourly["weather"][0]["id"] for hourly in data_hourly]
#
# will_rain = False
#
# for check in data_hourly_codes:
# 	if check < 900:
# 		will_rain = True
#
# if will_rain:
# 	print("bring an Umbrella")
#
# if will_rain:
# 	message = client.messages.create(
# 		from_='whatsapp:+14155238886',
# 		body='Bring an Umbrella',
# 		to='whatsapp:+380661508739'
# 	)
# 	print(message.sid)
#
# else:
# 	message = client.messages.create(
# 		from_='whatsapp:+14155238886',
# 		body='No rain',
# 		to='whatsapp:+380661508739'
# 	)
# 	print(message.sid)
