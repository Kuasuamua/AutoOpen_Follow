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
import ctypes
def ensure_caps_lock_off():
    # Define the necessary constants
    VK_CAPITAL = 0x14
    KEYEVENTF_EXTENDEDKEY = 0x1
    KEYEVENTF_KEYUP = 0x2

    # Load the user32.dll
    user32 = ctypes.windll.user32
    # Check if Caps Lock is on
    if user32.GetKeyState(VK_CAPITAL):
        # If Caps Lock is on, turn it off
        user32.keybd_event(VK_CAPITAL, 0x45, KEYEVENTF_EXTENDEDKEY, 0)
        user32.keybd_event(VK_CAPITAL, 0x45, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, 0)
        print("Caps Lock has been turned OFF")
    else:
        print("Caps Lock is already OFF")


# Call the function to ensure Caps Lock is off
# 如果键盘是大写状态，URL在地址栏跳转后，网页呈现无法打开状态。所以，要确保键盘是小写状态。
#pyautogui.hotkey('win', 'd')
time.sleep(0.25)  # Number of seconds
ensure_caps_lock_off()