# LinkedIN Automatically Search Jobs and Apply Project
# Created by: @CemRoot


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

s = Service("C:/Users/eminc/Documents/chromedriver")
o = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=o)

driver.get('https://www.linkedin.com/jobs/search')
driver.maximize_window()

# find sign in button
time.sleep(2)
sign_in = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
sign_in.click()
# Wait and loging to LinkedIn
time.sleep(3)
email = driver.find_element(By.ID, 'username')
email.send_keys(os.getenv('EMAIL'))
password = driver.find_element(By.ID, 'password')
password.send_keys(os.getenv('PASSWORD'))
login = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large")
login.click()
# Fill the search box
search_box = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__text-input")
search_box.send_keys('Python Developer Intern')

# Enter the search box
search_button = driver.find_element(By.CSS_SELECTOR, ".jobs-search-box__submit-button")
search_button.click()

