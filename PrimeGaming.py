""" This script can add subscriber to prime games"""
import random
import time
import pathlib
import gspread
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

chrome_options = Options()
# scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")


#
# chrome_options.add_argument("--user-data-dir=chrome-data")
# chrome_options.add_argument('--profile-directory=Profile 8')
# prefs = {"profile.default_content_setting_values.notifications": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("user-data-dir=chrome-data")
# chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome("Driver/chromedriver.exe", chrome_options=chrome_options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Time Counting
StartTime = time.time()
print("This Script Start " + time.ctime())


# driver.get("https://accounts.google.com/")
driver.get("https://accounts.google.com/?hl=en-us")
time.sleep(4)


def enter_email_password(driver, username, password):
    driver.implicitly_wait(10)
    email_xpath = "//input[@type='email']"
    driver.find_element_by_xpath(email_xpath).send_keys(username)

    print(input("Try Manually :"))

    driver.implicitly_wait(10)
    time.sleep(4)
    next_button_xpath = "//span[contains(.,'Next')]/parent::button"
    # next_button = driver.find_element_by_xpath(next_button_xpath)
    # next_button.click()
    # time.sleep(4)

    print(input("Try Manually :"))

    driver.implicitly_wait(10)
    password_xpath = "//input[@type='password']"
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    driver.find_element_by_xpath(next_button_xpath).click()

    driver.implicitly_wait(10)
    driver.get("https://mail.google.com/mail/u/0/")


# enter_email_password(driver, "johnalis841@gmail.com", "globe0112358")


print(input("Google Login Done ....:\n"))
driver.get("https://www.twitch.tv/")
time.sleep(4)

print(input("twitch Login Done ....\n"))
driver.get("https://www.amazon.com/your-account")
time.sleep(4)

driver.get("https://gaming.amazon.com/intro")
time.sleep(4)
