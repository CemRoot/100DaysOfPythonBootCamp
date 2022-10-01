# Twitter Competition Bot

from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 50
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Users/eminc/Documents/chromedriver"
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
	def __init__(self):
		self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
		self.up = 0
		self.down = 0

	def repeat(self):
		while True:
			self.get_internet_speed()
			if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
				self.tweet_at_provider()

			else:
				for i in range(40):
					print("Internet speed is good!")
					sleep(1)
					print(f"Program  will restart after {40 - i} seconds...")

	def get_internet_speed(self):
		self.driver.get("https://www.speedtest.net")
		start_test = self.driver.find_element(By.CLASS_NAME, "start-text")
		start_test.click()
		print("Speed Test starting...")
		for i in range(45):
			sleep(1)
			print(f"Waiting {45 - i} seconds...")
		print("Speed Test complete!")

		self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
		self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
		print(f"down: {self.down}\nup: {self.up}")
		sleep(3)

	def tweet_at_provider(self):
		self.driver.get("https://twitter.com/login")
		print("Going to Twitter...")
		sleep(3)
		# Login
		try:
			username = self.driver.find_element(By.NAME, 'text')
			username.send_keys(TWITTER_EMAIL)
			username.send_keys(Keys.ENTER)
			sleep(3)

			password = self.driver.find_element(By.NAME, 'password')
			password.send_keys(TWITTER_PASSWORD)
			password.send_keys(Keys.ENTER)
			sleep(3)
		except NoSuchElementException:
			print("Already logged in")

		try:
			print("Security Processing...")
			bot.tweet_sender()
		except NoSuchElementException:
			# Write Number
			print("Security Processing...")
			phone_number = self.driver.find_element(By.NAME, 'text')
			phone_number.send_keys(os.getenv("SECN"))
			phone_number.send_keys(Keys.ENTER)
			sleep(3)
			print("Security Processing Complete!")
			bot.tweet_sender()
		else:
			print("else basıldı. excepten sonra ")

	def tweet_sender(self):
		# Compose and send Tweet
		message = f"Test tweet for DAY51 of #100DaysofPython Twitter bot: Hey Internet Provider! " \
		          f"Why is my internet speed {self.down} down/{self.up} up when I pay " \
		          f"for {PROMISED_DOWN} down/{PROMISED_UP} up?"
		compose_tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
		compose_tweet.send_keys(message)
		sleep(2)
		send_tweet = self.driver.find_element(By.XPATH, '//*[text()="Tweet"]')
		send_tweet.click()
		print("Tweet sent!")


bot = InternetSpeedTwitterBot()
bot.repeat()
