from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# assert "Python" in driver.title
# x_path = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# x_path.click()
# print(x_path.text)

time.sleep(4)

all_portals = driver.find_element(By.LINK_TEXT, "Commons")
# all_portals.click()
time.sleep(4)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(4)
