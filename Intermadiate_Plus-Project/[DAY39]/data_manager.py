from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:

	def __init__(self):
		self.destination_data = {}

	def get_destination_data(self):
		response = requests.get(url=os.environ['SHEETY_PRICES_ENDPOINT'])
		data = response.json()
		self.destination_data = data["prices"]
		return self.destination_data

	def update_destination_codes(self):
		for city in self.destination_data:
			new_data = {
				"price": {
					"iataCode": city["iataCode"]
				}
			}
			response = requests.put(
				url=f"{os.environ['SHEETY_PRICES_ENDPOINT']}/{city['id']}",
				json=new_data
			)
			print(response.text)

  def get_customer_emails(self):

    customers_endpoint = os.environ['SHEETY_PRICES_ENDPOINT']
    response = requests.get(url=customers_endpoint)
    data = response.json()
    self.customer_data = data["users"]
    return self.customer_data