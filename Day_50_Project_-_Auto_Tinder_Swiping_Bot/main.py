from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions	import NoSuchElementException, ElementClickInterceptedException
from time import sleep

fb_email = "azamat.salamatov2004@gmail.com"
fb_password = "SALazaCHEM2004"

driver = webdriver.Chrome()
driver.get("http://www.tinder.com")
sleep(2)

login_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_btn.click()
sleep(2)

fb_login = driver.find_element(By.XPATH	, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window	)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH	, '//*[@id="pass"]')

email.send_keys(fb_email)
password.send_keys(fb_password)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base)
print(driver.title)
sleep(5)

allow_loc_btn = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_loc_btn.click()
notif_btn = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notif_btn.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
	sleep(1)

	try:
		print("called")
		like_btn = drive.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
		like_btn.click()

	except ElementClickInterceptedException:
		try:
			match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
			match_popup.click()
		except NoSuchElementException:
			sleep(2)

driver.quit()
