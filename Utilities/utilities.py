from urllib.request import *
from urllib.error import *
import Xpath
import os
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
def intro():
    os.system("cls")
    print("""
888      d8b          888                    888 8888888               888888b.            888    
888      Y8P          888                    888   888                 888  "88b           888    
888                   888                    888   888                 888  .88P           888    
888      888 88888b.  888  888  .d88b.   .d88888   888   88888b.       8888888K.   .d88b.  888888 
888      888 888 "88b 888 .88P d8P  Y8b d88" 888   888   888 "88b      888  "Y88b d88""88b 888    
888      888 888  888 888888K  88888888 888  888   888   888  888      888    888 888  888 888    
888      888 888  888 888 "88b Y8b.     Y88b 888   888   888  888      888   d88P Y88..88P Y88b.  
88888888 888 888  888 888  888  "Y8888   "Y88888 8888888 888  888      8888888P"   "Y88P"   "Y888 


                                                                             [Made by: Tal Hasson]


---------------------------------------------------------------------------------------------------
Please notice: after the browser has been launched come back and follow the instructions. 
---------------------------------------------------------------------------------------------------
""")
    time.sleep(1.5)


def check_internet_connection():
    print("\nTesting internet connection and website status...")
    try:
        urlopen('http://216.58.192.142', timeout=10)
        try:
            urlopen("https://www.linkedin.com/home", timeout=2)
            print("Everything is set to go!")
            return True
        except URLError:
            print("[-] LinkedIn might be offline...")
            return False
    except URLError:
        print("[-] No internet connection...")
        return False


def two_factor_auth():
    print("[+] Successfully signed in!")
    try:
        two_factor = input("\n[*] If you have 2FA please enter the verification code."
                           "\nWhen you are in LinkedIn Homepage press Enter to continue: ")
        while two_factor != "":
            two_factor = input("Please press Enter")
    except:
        pass
