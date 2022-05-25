"""
Library Documentation : https://pyautogui.readthedocs.io/en/latest/index.html ,
"""

import pyautogui
import time
import random
import pyperclip
from playsound import playsound


screen_size = pyautogui.size()
print(screen_size)

speed_frequency = 4

# print(input("press enter to start:"))

open_browser_move_x = 710
open_browser_move_y = 1058
open_browser_move = pyautogui.moveTo(open_browser_move_x, open_browser_move_y)
time.sleep(speed_frequency)
pyautogui.click()

# print(input("Select Profile:"))

open_profile_move_x = 691
open_profile_move_y = 606
open_profile_move = pyautogui.moveTo(open_profile_move_x, open_profile_move_y)
time.sleep(speed_frequency)
pyautogui.click()

# print(input("Maximize:"))
pyautogui.hotkey('Alt', 'Space', 'x')

# print(input("Enter Gmail Url:"))

open_gmail_move_x = 146
open_gmail_move_y = 51
gmail_url_move = pyautogui.moveTo(open_gmail_move_x, open_gmail_move_y)
time.sleep(speed_frequency)
pyautogui.click()

gmail_link = "https://mail.google.com/mail/"
pyautogui.typewrite(f'{gmail_link}\n', interval=.001)

print(input("Enter TwisTv Url:"))
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

open_twistTv_move_x = 146
open_twistTv_move_y = 51
twistTv_url_move = pyautogui.moveTo(open_twistTv_move_x, open_twistTv_move_y)
time.sleep(speed_frequency)
pyautogui.click()

twitch_link = "https://www.twitch.tv/twistv"
pyautogui.typewrite(f'{twitch_link}\n', interval=.001)



