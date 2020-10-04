from Utilities.utilities import *
from settings import *


class LinkedInLogin:
    def __init__(self):
        self.path = CHROME_PATH
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.maximize_window()

    def get_linkedin(self):
        self.open_browser()
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        time.sleep(1)

    def login_linkedin(self):
        self.get_linkedin()
        print("\n[*] Please wait, trying to sign in to LinkedIn...")
        try:
            self.driver.find_element_by_id("username").send_keys(email)
            time.sleep(1)
            self.driver.find_element_by_id("password").send_keys(password)
            time.sleep(1)
            self.driver.find_element_by_xpath(Xpath.SIGN_IN_BUTTON).click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
                By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
        except:
            pass
