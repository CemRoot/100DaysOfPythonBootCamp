from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

URL = "https://tinder.com/"

driver_path = Service("C:/Users/eminc/Documents/chromedriver")
# create a driver object for chrome
driver = webdriver.Chrome(service=driver_path)
my_number = 5426608739
# Open the URL
driver.get(URL)
driver.maximize_window()
time.sleep(2)
# Accept cookies
driver.find_element(By.XPATH, "//*[@id='o-98920890']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]").click()
time.sleep(2)
# Click on the login button
login_button = driver.find_element(By.XPATH, "//*[text()='Log in']")
login_button.click()
# Click on the login with phone number button
time.sleep(2)
login_with_phone_number_button = driver.find_element(By.XPATH, "//*[text()='Log in with phone number']")
login_with_phone_number_button.click()
# Enter the phone number
time.sleep(5)
phone_number = driver.find_element(By.XPATH, "//*[@name='phone_number']")
phone_number.send_keys(my_number)
# Click on the continue button
continue_button = driver.find_element(By.XPATH, "//*[text()='Continue']")
continue_button.click()
# Enter the code
time.sleep(5)


def enter_code():
	i = 1
	your_sms_code = input("Enter the code: ")
	while i <= 6:
		for j in your_sms_code:
			# input []
			code = driver.find_element(By.XPATH, f"//*[@id='o-1827301966']/main/div/div[1]/div/div[3]/input[{i}]")
			code.send_keys(j)
			time.sleep(2)
			i += 1


error = '//*[@id="codeVerificationErrorMessage"]/div'
enter_code()
driver.find_element(By.XPATH, "//*[text()='Continue']").click()
try:
	driver.find_element(By.XPATH, error)
	print("Wrong code")
	enter_code()
except NoSuchElementException:
	print("Correct code")
# enter_code()
# driver.find_element(By.XPATH, "//*[text()='Continue']").click()
# # if the code is wrong
#
#
# print("Wrong code. Try again.")
# enter_code()
#
# print("Code accepted.")

# email code
time.sleep(5)
email_code = input("Enter the code: ")
e = 1
while e <= 6:
	for z in email_code:
		# input []
		code = driver.find_element(By.XPATH, f"//*[@id='o-1827301966']/main/div/div[1]/div/div[3]/input[{e}]")
		code.send_keys(z)
		time.sleep(2)
		e += 1
# Click on the continue button
continue_button = driver.find_element(By.XPATH, "//*[text()='Confirm Email']")
continue_button.click()
# Allow location
time.sleep(5)
driver.find_element(By.XPATH, "//*[text()='Allow']").click()
# Allow notifications
time.sleep(2)
driver.find_element(By.XPATH, "//*[text()='Enable']").click()
# Click on the like button
time.sleep(2)
your_likes = 0
while your_likes <= 50:
	try:
		like_button = driver.find_element(By.XPATH,
		                                  "//*[@id='o-1827301966']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button")
		like_button.click()
		your_likes += 1
		time.sleep(2)
	except NoSuchElementException:
		print("You have no more likes")
		break
print(f"You have liked {your_likes} people")
