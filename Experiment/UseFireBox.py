import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



desired = DesiredCapabilities().FIREFOX
desired["marionette"] = False
driver = webdriver.Firefox(capabilities=desired, executable_path="../Driver/geckodriver.exe")


driver.get('https://accounts.google.com/?hl=en-us')

# driver = webdriver.Chrome("../Driver/geckodriver.exe")

# profile = webdriver.FirefoxProfile(
#     '/Users/user/Library/Application Support/Firefox/Profiles/w4wak6ii.default')
# profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
# profile.update_preferences()
# # desired = DesiredCapabilities.FIREFOX
#
# driver = webdriver.Firefox(firefox_profile=profile, capabilities=desired,
#                            executable_path="../Driver/geckodriver.exe")
#
# driver.get("https://www.google.com")


driver.implicitly_wait(10)
email_xpath = "//input[@type='email']"
driver.find_element_by_xpath(email_xpath).send_keys("johnalis841@gmail.com")

print(input("Try Manually :"))

driver.implicitly_wait(10)
time.sleep(4)
# next_button_xpath = "//span[contains(.,'Next')]/parent::button"
# next_button = driver.find_element_by_xpath(next_button_xpath)
# next_button.click()
# time.sleep(4)

print(input("Try Manually :"))

driver.implicitly_wait(10)
password_xpath = "//input[@type='password']"
driver.find_element_by_xpath(password_xpath).send_keys("globe0112358")
# driver.find_element_by_xpath(next_button_xpath).click()

driver.implicitly_wait(10)
driver.get("https://mail.google.com/mail/u/0/")