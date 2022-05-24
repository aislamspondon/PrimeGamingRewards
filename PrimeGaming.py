""" This script can add subscriber to prime games"""
import time

from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")


driver.get("https://mail.google.com/")
time.sleep(4)

driver.get("https://www.twitch.tv/")
time.sleep(4)

driver.get("https://www.amazon.com/your-account")
time.sleep(4)

driver.get("https://gaming.amazon.com/intro")
time.sleep(4)
