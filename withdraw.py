from utilities import *
from linkedinlogin import LinkedInLogin


class LinkedInWithdraw(LinkedInLogin):
    def __init__(self):
        super().__init__()

    def nav(self):
        self.login_linkedin()
        time.sleep(2)
        self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
        time.sleep(1)

    def withdraw(self, num):
        self.nav()
        counter = 0
        while counter < int(num):
            try:
                for button in range(counter, int(num)):
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, '//button[@data-control-name="withdraw_single"]'))).click()
                    WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                        (By.XPATH, '//button[@class="artdeco-modal__confirm-dialog-btn artdeco-button'
                                   ' artdeco-button--2 artdeco-button--primary ember-view"]'))).click()
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


b = LinkedInWithdraw()
b.withdraw(3)
# TODO: withdraw invitations according to period time
