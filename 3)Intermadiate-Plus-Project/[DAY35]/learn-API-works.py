import requests
import pandas

api_key = "YOUR API KEY"
MY_LONGITUDE = "36.896893"
MY_LATITUDE = "30.713324"

parameters = {
	"lat": MY_LATITUDE,
	"lon": MY_LONGITUDE,
	"appid": api_key,
	"exclude": "current,minutely,daily",
	"lang": "tr",
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
res.raise_for_status()
data_weather = res.json()

# TODO: Practie printing out the weather ID for the weather in the 0th hour.
print(data_weather["hourly"][0]["weather"][0]["id"])

# TODO: Try to create a slice from the weather data to get a list of the hourly forecasts for only the next 12 hours.
data_hourly = data_weather["hourly"][:12]
print(data_hourly)
# TODO: Using the above try to create a list of only the next 12 weather condition codes.
data_hourly_codes = [hourly["weather"][0]["id"] for hourly in data_hourly]
print(data_hourly_codes)
# TODO: print "bring an Umbrella" if any of the next 12 hourly weather condition codes is less than 700
will_rain = False
for check in data_hourly_codes:
	if check < 900:
		will_rain = True

if will_rain:
	print("bring an Umbrella")

from twilio.rest import Client

account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"
client = Client(account_sid, auth_token)

if will_rain:
	message = client.messages.create(
		from_='whatsapp:+14155238886',
		body='Bring an Umbrella',
		to='whatsapp:+380661508739'
	)
	print(message.sid)

else:
	message = client.messages.create(
		from_='whatsapp:+14155238886',
		body='No rain',
		to='whatsapp:+380661508739'
	)
	print(message.sid)
