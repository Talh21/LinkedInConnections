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

    def withdraw(self, num):  # Should go TO the last page/end of the page first
        counter = 0
        while counter < int(num):
            try:
                for button in range(counter, int(num)):
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, Xpath.WITHDRAW_INVITATION))).click()
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH,Xpath.CONFIRM_WITHDRAWAL))).click()
                    counter += 1
                    print(f"\r[+] Successfully withdraw invitation => #{counter}", end='', flush=True)
                    time.sleep(1)
            except:
                pass

            self.driver.execute_script('window.scrollTo(0,(window.pageYOffset+300))')
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath(Xpath.NEXT_PAGE).click()
                time.sleep(1)
            except:
                pass

        self.driver.quit()
        print("\nProcess done!")

    def main(self):
        if check_internet_connection():
            try:
                number_of_withdraws = self.get_number_of_wanted_withdraws()
                self.nav()
                self.withdraw(number_of_withdraws)
            except:
                print("\n[-] Quitting...")
                sys.exit()


# TODO: withdraw invitations according to period time
