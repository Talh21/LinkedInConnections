from Bot.linkedinlogin import LinkedInLogin
from Utilities.validation import *
from Utilities.utilities import *


class LinkedInWithdraw(LinkedInLogin):
    def __init__(self):
        super().__init__()
        self.num = ""

    def nav(self):
        self.login_linkedin()
        two_factor_auth()
        time.sleep(2)
        self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
        time.sleep(1)

    def get_number_of_wanted_withdraws(self):
        self.num = input("\nPlease enter the number of invites that you wish to withdraw: ")
        while check_if_isdigit(self.num) is False:
            self.num = input("\nNot a valid number. Try again: ")
        return self.num

    def go_to_last_page(self):
        while True:
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, Xpath.NEXT_PAGE))).click()
            except TimeoutException:
                print("\nLast page")
                break

    def withdraw(self, num):
        counter = 0
        while counter < int(num):
            all_withdraws_btn = WebDriverWait(self.driver, 7).until(EC.presence_of_all_elements_located(
                (By.XPATH, Xpath.WITHDRAW_INVITATION)))
            try:
                for button in range(counter, int(num)):
                    withdraw = all_withdraws_btn[-1]
                    withdraw.click()
                    WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.XPATH, Xpath.CONFIRM_WITHDRAWAL))).click()
                    time.sleep(3)  # Load the next withdraw
                    counter += 1
                    print(f"\r[+] Successfully withdraw invitation => #{counter}", end='', flush=True)

            except:
                pass

            if counter < int(num) and len(all_withdraws_btn) == 0:
                try:
                    self.driver.find_element_by_xpath(Xpath.PREVIOUS_PAGE).click()
                    time.sleep(2)

                except:
                    pass

        self.driver.quit()
        print("\nProcess done!")

    def main(self):
        if check_internet_connection():
            try:
                number_of_withdraws = self.get_number_of_wanted_withdraws()
                self.nav()
                self.go_to_last_page()
                self.withdraw(number_of_withdraws)

            except:
                print("\n[-] Quitting...")
                sys.exit()
