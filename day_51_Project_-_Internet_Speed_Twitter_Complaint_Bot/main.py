from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

TWITTER_EMAIL = "your.email.com"
TWITTER_PASSWORD = "YourPassword"

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, '.start-button a')
        go_btn.click()
        sleep(20)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        sleep(20)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        try:
            self.driver.get("https://twitter.com/i/flow/login")
            sleep(4)
            email_field = self.driver.find_element(By.XPATH,
                                                   '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
            sleep(4)
            email_field.click()
            email_field.send_keys(TWITTER_EMAIL)
            email_field.send_keys(Keys.ENTER)
            sleep(4)
            password_field = self.driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            sleep(2)
            password_field.send_keys(TWITTER_PASSWORD)
            password_field.send_keys(Keys.ENTER)

            tweet = f"Hey Internet provider, why my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[1]/div[1]/div/aside/div/a/div')
            tweet_button.click()
            tweet_compose = self.driver.find_element(By.XPATH,
                                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/textarea')
            tweet_compose.send_keys(tweet)
            sleep(3)

            tweet_send_btn = self.driver.find_element(By.XPATH,
                                                      '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div/div')
            tweet_send_btn.click()

            self.driver.quit()
        except:
            print("Unfortunately, twitter doesn't want to be controlled by a bot:(")


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
