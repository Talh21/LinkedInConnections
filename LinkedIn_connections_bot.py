from credentials import *
from validation import *
from selenium import webdriver
import time
from urllib.request import *
from urllib.error import *
import os
import sys


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
    time.sleep(1)


def check_internet_connection():
    try:
        urlopen('http://216.58.192.142', timeout=10)
        try:
            urlopen("https://www.linkedin.com/home", timeout=2)
            return True
        except URLError:
            print("[-] LinkedIn might be offline...")
            return False
    except URLError:
        print("[-] No internet connection...")
        return False


def get_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", dest="number", type=check_if_positive,
                        help="Specify the number of connections you want to send a request to.")
    options = parser.parse_args()
    if not options.number:
        parser.error('[-] You must enter a valid number. \n[*] Type "-h/--help" for more info')
    return options


def get_linkedin():
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    driver.maximize_window()
    time.sleep(1)


def login():
    email, password = get_credentials()
    try:
        driver.find_element_by_id("username").send_keys(email)
        time.sleep(1)
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]').click()
    except:
        pass


def two_factor_auth():
    try:
        two_factor = input("If you you have 2FA please enter the verification code."
                   "\nWhen you are in LinkedIn Homepage press Enter to continue: ")
        while two_factor != "":
            two_factor = input("Please press Enter")
    except:
        pass


def network_send_requests(number_of_connections):
    time.sleep(2)
    driver.find_element_by_xpath('//header[@data-control-name="overlay.minimize_connection_list_bar"]').click()
    driver.get('https://www.linkedin.com/mynetwork/')
    x_path = '//button[@data-control-name="invite"]'
    counter = 0
    while counter < int(number_of_connections):
        driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
        time.sleep(4)
        try:
            for button in range(counter, int(number_of_connections)):
                button = driver.find_element_by_xpath(x_path)
                button.click()
                counter += 1
                print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                time.sleep(1)
        except:
            pass

    driver.quit()
    print("\nProcess done!")


if __name__ == '__main__':
    try:
        number_of_connections_to_add = get_option()
        intro()
        if check_internet_connection():
            try:
                chrome_path = "C:\Program Files\chromedriver.exe"
                driver = webdriver.Chrome(executable_path=chrome_path)
                get_linkedin()
                login()
                two_factor_auth()
                network_send_requests(number_of_connections_to_add.number)
            except:
                print("\n[-] Quitting...")
    except:
        print("\n[-] Quitting...")
        sys.exit()
