import tkinter as tk
import pyautogui
import requests
import datetime
from datetime import datetime, timezone
#import os
import time
import pyperclip
import os
import shutil
#import nltk
import re
#from googletrans import Translator
from textblob import TextBlob
import win32api
import win32gui
import win32con
import pyautogui
import requests
import datetime
from datetime import datetime, timezone
#import os
import time
import pyperclip
import os
import shutil
#import nltk
import re
#from googletrans import Translator
from textblob import TextBlob
import win32api
import win32gui
import win32con



def AutoOpen_Follow():
    from FC_switch_to_english import switch_to_english
    from Turn_off_CapsLock import ensure_caps_lock_off

    switch_to_english()
    ensure_caps_lock_off()
    time.sleep(0.25)  # Number of seconds
    pyautogui.hotkey('win', 'd')
    time.sleep(0.25)  # Number of seconds
    print('移动到快捷方式并打开中......')
    # pyautogui.doubleClick(x=45, y=745)
    time.sleep(1)  # Number of seconds must be wait
    pyautogui.hotkey('win')
    time.sleep(1)  # Number of seconds
    # pyautogui.click(269, 60)
    # time.sleep(1)  # Number of seconds
    pyautogui.typewrite('Follow', interval=0.025)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)

    # click twitter
    pyautogui.moveTo(70, 78, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    # click picture
    pyautogui.moveTo(110, 78, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    # click video
    pyautogui.moveTo(150, 78, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(5)

    # click profile
    pyautogui.moveTo(229, 28, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    # click profile
    pyautogui.moveTo(206, 117, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)

    # click profile
    pyautogui.moveTo(784, 428, duration=0.5)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)

    # close Follow
    pyautogui.moveTo(1890, 21, duration=2.5)
    time.sleep(1)
    pyautogui.click()