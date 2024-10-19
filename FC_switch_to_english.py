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


def switch_to_english():
    # Get the handle of the foreground window
    hwnd = win32gui.GetForegroundWindow()

    # English (United States) language code
    ENGLISH_UNITED_STATES = 0x0409

    # Load the English keyboard layout
    result = win32api.LoadKeyboardLayout("00000409", win32con.KLF_ACTIVATE)

    if result:
        # Post a message to the window to change the keyboard layout
        win32api.SendMessage(hwnd, win32con.WM_INPUTLANGCHANGEREQUEST, 0, result)
        print("Input method switched to English.")
    else:
        print("Failed to switch input method.")

    # Give some time for the change to take effect
    time.sleep(1)


switch_to_english()