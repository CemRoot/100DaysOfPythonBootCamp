from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Chrome_driver_path = Service("C:\\Users\\eminc\\Documents\\chromedriver")
driver = webdriver.Chrome(service=Chrome_driver_path)

driver.get("https://www.python.org/")
""" find_element_by_id - find the element by id attribute"""
# price = driver.find_element(By.ID,"priceblock_ourprice")
# print(price.text)

""" driver.find_element(By.ID,) --its mean find the element by id attribute"""
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

""""find to logo image by class name"""
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
"""Find link 'href' css  """
documentation_link = driver.find_element(By.CSS_SELECTOR, "#documentation > a")
print(documentation_link.text)


""" Close driver if you want to close  active tab """
# driver.close()
""" Close all tabs """
driver.quit()