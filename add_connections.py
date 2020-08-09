from utilities import *
from validation import *
from browser import Browser


class LinkedInAdd(Browser):
    def __init__(self):
        super().__init__()
        self.mode = ""
        self.keyword = ""
        self.num = ""

    def user_prompt_for_choosing_mode(self):
        self.mode = input("""\nDo you want to use auto-pilot version or search by specific keyword?
1) Auto-pilot
2) Search by keyword
Choice: """)

        while is_choice_is_valid(self.mode) is False:
            self.mode = input("""Not a valid option. Please Try again.\n
1) Auto-pilot
2) Search by keyword
Choice: """)

        return self.mode

    def get_num_of_connections_auto(self):
        self.num = input("\nPlease enter the number of connections you want to send a request to: ")
        while check_if_isdigit(self.num) is False:
            self.num = input("\nNot a valid number. Try again: ")
        return self.num

    def get_the_number_of_connections_and_keyword(self):
        self.keyword = input("\nPlease choose the keyword: ")
        while check_if_input_is_empty(self.keyword) is False:
            self.keyword = input("[-] Error! You must enter a keyword\nTry again:")
        self.num = input("Please enter the number of connections you want to send a request to: ")
        while check_if_isdigit(self.num) is False:
            self.num = input("\nNot a valid number. Try again: ")
        return self.keyword, self.num

    def network_send_requests(self, num):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
        self.driver.get('https://www.linkedin.com/mynetwork/')
        counter = 0
        try:
            for connection in range(counter, int(num)):
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                    By.XPATH, Xpath.CONNECT_NETWORK_UP_PAGE))).click()
                counter += 1
                print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                time.sleep(2)
        except:
            pass

        while counter < int(num):
            self.driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
            time.sleep(4)
            try:
                for connection in range(counter, int(num)):
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
                        By.XPATH, Xpath.INVITE_CONNECTIONS_NETWORK_PAGE))).click()
                    counter += 1
                    print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                    time.sleep(2)
            except:
                pass

        self.driver.quit()
        print("\nProcess done!")

    def search_connections_by_keyword(self, keyword):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, Xpath.SEARCH_BOX)))
        search_box.send_keys(keyword, Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, Xpath.VIEW_ONLY_PEOPLE)))

    def send_request_by_keyword(self, keyword, num):
        self.search_connections_by_keyword(keyword)
        counter = 0
        while counter < int(num):
            try:
                for button in range(counter, int(num)):
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, Xpath.CONNECT_BUTTON_SEARCH_PAGE))).click()
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, Xpath.CONFIRM_CONNECTION))).click()
                    counter += 1
                    print(f"\r[+] Sent a connection request => #{counter}", end='', flush=True)
                    time.sleep(1)
            except:
                pass

            self.driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
            time.sleep(4)
            try:
                self.driver.find_element_by_xpath(Xpath.NEXT_PAGE).click()
                time.sleep(1)
            except:
                pass

        self.driver.quit()
        print("\nProcess done!")

    def main(self):
        intro()
        if check_internet_connection():
            try:
                mode = self.user_prompt_for_choosing_mode()
                if mode == "1":
                    number_of_connections = self.get_num_of_connections_auto()
                    self.login_linkedin()
                    two_factor_auth()
                    self.network_send_requests(number_of_connections)
                keyword, number_of_connections = self.get_the_number_of_connections_and_keyword()
                self.login_linkedin()
                two_factor_auth()
                self.send_request_by_keyword(keyword, number_of_connections)

            except:
                print("\n[-] Quitting...")
                sys.exit()


if __name__ == '__main__':
    linkedin_bot = LinkedInAdd()
    linkedin_bot.main()
