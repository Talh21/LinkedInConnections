from utilities import *


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


def user_prompt_for_choosing_mode():
    auto_or_search = input("""\nDo you want to use auto-pilot version or search by specific keyword?
1) Auto-pilot
2) Search by keyword
Choice: """)

    while is_choice_is_valid(auto_or_search) is False:
        auto_or_search = input("""Not a valid option. Please Try again.\n
1) Auto-pilot
2) Search by keyword
Choice: """)

    return auto_or_search


def get_the_number_of_connections_and_keyword():
    key_word = input("\nPlease choose the keyword: ")
    number_of_requests = input("Please enter the number of connections you want to send a request to: ")
    while check_if_isdigit(number_of_requests) is False:
        number_of_requests = input("\nNot a valid number. Try again: ")
    return key_word, number_of_requests


def get_num_of_connections_auto():
    number_of_requests = input("\nPlease enter the number of connections you want to send a request to: ")
    while check_if_isdigit(number_of_requests) is False:
        number_of_requests = input("\nNot a valid number. Try again: ")
    return number_of_requests


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


def network_send_requests(number_of_connections):
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
    driver.get('https://www.linkedin.com/mynetwork/')
    counter = 0
    try:
        for connection in range(counter, int(number_of_connections)):
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((
                By.XPATH, Xpath.CONNECT_NETWORK_UP_PAGE))).click()
            counter += 1
            print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
            time.sleep(2)
    except:
        pass

    while counter < int(number_of_connections):
        driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
        time.sleep(4)
        try:
            for connection in range(counter, int(number_of_connections)):
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((
                    By.XPATH, Xpath.INVITE_CONNECTIONS_NETWORK_PAGE))).click()
                counter += 1
                print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                time.sleep(2)
        except:
            pass

    driver.quit()
    print("\nProcess done!")


def search_connections_by_keywords(key_word):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, Xpath.SEARCH_BOX)))
    search_box.send_keys(key_word, Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, Xpath.VIEW_ONLY_PEOPLE)))


def sent_request_by_keyword(number_of_connections):
    counter = 0
    while counter < int(number_of_connections):
        try:
            for button in range(counter, int(number_of_connections)):
                WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                    (By.XPATH, Xpath.CONNECT_BUTTON_SEARCH_PAGE))).click()
                WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                    (By.XPATH, Xpath.CONFIRM_CONNECTION))).click()
                counter += 1
                print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                time.sleep(1)
        except:
            pass

        driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
        time.sleep(4)
        try:
            driver.find_element_by_xpath(Xpath.NEXT_PAGE).click()
            time.sleep(1)
        except:
            pass

    driver.quit()
    print("\nProcess done!")


def main():
    get_linkedin()
    login()
    two_factor_auth()


if __name__ == '__main__':
    try:
        intro()
        mode = user_prompt_for_choosing_mode()
        if check_internet_connection():
            try:
                if mode == "2":
                    keyword, number = get_the_number_of_connections_and_keyword()
                    chrome_path = "C:\Program Files\chromedriver.exe"
                    driver = webdriver.Chrome(executable_path=chrome_path)
                    main()
                    search_connections_by_keywords(keyword)
                    sent_request_by_keyword(number)
                else:
                    number = get_num_of_connections_auto()
                    chrome_path = "C:\Program Files\chromedriver.exe"
                    driver = webdriver.Chrome(executable_path=chrome_path)
                    main()
                    network_send_requests(number)
            except:
                print("\n[-] Quitting...")
    except:
        print("\n[-] Quitting...")
        sys.exit()

