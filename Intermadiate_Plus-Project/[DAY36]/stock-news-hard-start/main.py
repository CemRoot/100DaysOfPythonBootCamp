import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
client = Client(account_sid, auth_token)


load_dotenv


parametres_stock = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK,
	"interval": "daily",
	"apikey": stock_api_key,
}
response_stock = requests.get(STOCK_ENDPOINT, params=parametres_stock)
data_stock = response_stock.json()
price_today = data_stock["Time Series (Daily)"][list(data_stock["Time Series (Daily)"])[4]]["4. close"]
price_yesterday = data_stock["Time Series (Daily)"][list(data_stock["Time Series (Daily)"])[1]]["4. close"]

parameters_news = {
	"q": STOCK,
	"apiKey": news_api_key,
}
response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
data = response_news.json()
articles = data["articles"]
three_articles = articles[:3]
formatted_articles = [f"{article['title']}. \nBreif: {article['description']}" for article in three_articles]
# Up or Down Emoji
if float(price_today) > float(price_yesterday):
	emoji = "⬆ ↓"
else:
	emoji = "↓"
if float(price_today) > float(price_yesterday) * 1.05 or float(price_today) < float(price_yesterday) * 0.95:
	for article in formatted_articles:
		message = client.messages.create(
			from_='whatsapp:+14155238886',
			body=f"{emoji} {COMPANY_NAME} {price_today}\n" + article,
			to='whatsapp:+380661508739'
		)

		print(message.sid)


else:
	for article in formatted_articles:
		message = client.messages.create(
			from_='whatsapp:+14155238886',
			body="",
			to='whatsapp:+380661508739'
		)

		print(message.sid)
