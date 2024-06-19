# python main.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
# elem = driver.find_element(By.CLASS_NAME, "python-logo")
# print(elem.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# driver.find_elements()
#
# events = {}
# x_path = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# for i in range(len(x_path)):
#     s = x_path[i].text
#     s = s.split("\n")
#     print(s)
#     events[i] = {s[0]:s[1]}
#
# print(events)
#
