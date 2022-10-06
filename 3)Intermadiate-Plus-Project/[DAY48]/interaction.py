from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chrome_driver_path = Service("C:\\Users\\eminc\\Documents\\chromedriver")
driver = webdriver.Chrome(service=Chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click() -- if you want to click the element

# all_portals = driver.find_element(By.LINK_TEXT, "All portals") -find element by link text
search = driver.find_element(By.NAME, "search")  # find element by name
search.send_keys("Python")  # this mean send keys to search bar
search.send_keys(Keys.ENTER)  # this mean send enter key to search bar