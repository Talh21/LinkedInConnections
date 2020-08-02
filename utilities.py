from urllib.request import *
from urllib.error import *
from credentials import *
import os
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import Xpath


def is_choice_is_valid(answer):
    if answer == "1" or answer == "2":
        return True
    return False


def check_if_isdigit(inp):
    if inp.isdigit():
        return True
    return False


def check_internet_connection():
    print("Testing internet connections and website status...")
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
    try:
        two_factor = input("If you you have 2FA please enter the verification code."
                   "\nWhen you are in LinkedIn Homepage press Enter to continue: ")
        while two_factor != "":
            two_factor = input("Please press Enter")
    except:
        pass
