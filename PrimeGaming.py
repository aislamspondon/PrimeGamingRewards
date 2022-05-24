""" This script can add subscriber to prime games"""
import time

from selenium import webdriver
driver = webdriver.Chrome("Driver/chromedriver.exe")


driver.get("https://accounts.google.com/?hl=en-us")
time.sleep(4)


def login_gmail(username, password):
    button_xpath = "//tp-yt-paper-button[@aria-label='Sign in']"
    login_button = driver.find_elements_by_xpath(button_xpath)
    login_button[0].click()
    print(len(login_button))
    time.sleep(4)

    driver.implicitly_wait(10)
    # driver.get('https://accounts.google.com/')
    password_xpath = "//input[@type='email']"
    driver.find_element_by_xpath(password_xpath).send_keys(username)

    next_button_xpath = "//span[contains(.,'Next')]/parent::button"
    next_button = driver.find_element_by_xpath(next_button_xpath)
    next_button.click()
    print(next_button.text)
    time.sleep(4)


login_gmail("something@gmail.com", "12121212")


print(input("Google Login Done ....\n"))
driver.get("https://www.twitch.tv/")
time.sleep(4)

driver.get("https://www.amazon.com/your-account")
time.sleep(4)

driver.get("https://gaming.amazon.com/intro")
time.sleep(4)
