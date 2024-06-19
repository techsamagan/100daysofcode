LinkedIn_account = "althoughcorrect@gmail.com"
password = "AZAMAT2004"
PHONE = "3464731714"

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


driver = webdriver.Chrome()
# driver.get("https://www.linkedin.com/")
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3479411982&distance=25&f_AL=true&geoId=103743442&keywords=software%20developer")
sign_in_button_page1 = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_button_page1.click()

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys(LinkedIn_account)
email.send_keys(Keys.ENTER)
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
sleep(4)

all_jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_jobs_list:
	print("called")
	listing.click()
	sleep(2)

	try:
		apply_button = driver.find_element(By.CSS_SELECTOR, ".job-s-apply button")
		apply_button.click()
		sleep(5)

		# if phone is empty, then fill the phone number
		phone = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
		if phone.text=="":
			phone.send_keys(PHONE)
		
		submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

		# if the submit_button is a NEXT button, then this is a multistep application, skip it
		if submit_button.get_attribute("data-control-name") == "continue_unify":
			close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
			close_button.click()
			sleep(2)
			discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
			discard_button.click()
			print("Complex authentification, skipped")
			continue
		else:
			submit_button.click()

		sleep(2)
		close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
		close_button.click()


	except NoSuchElementException:
		print("No application button, skipped")
		continue

sleep(5)
driver.quit()
