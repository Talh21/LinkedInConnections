from utilities import *


class Browser:
    def __init__(self):
        self.path = "C:\Program Files\chromedriver.exe"
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
        try:
            self.driver.find_element_by_id("username").send_keys(email)
            time.sleep(1)
            self.driver.find_element_by_id("password").send_keys(password)
            time.sleep(1)
            self.driver.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]').click()
        except:
            pass
