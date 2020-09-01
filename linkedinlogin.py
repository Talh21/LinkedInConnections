from utilities import *
from selenium.webdriver.chrome.options import Options


CHROME_PATH = "C:\Program Files\chromedriver.exe"

"""
Mobile version implementation for future use:
MOBILE_UA = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F)' \
            #' AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
options = Options()
options.add_argument(f"user-agent={MOBILE_UA}")
self.driver = webdriver.Chrome(self.path, chrome_options=options)
"""


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
        try:
            self.driver.find_element_by_id("username").send_keys(email)
            time.sleep(1)
            self.driver.find_element_by_id("password").send_keys(password)
            time.sleep(1)
            self.driver.find_element_by_xpath('//button[@aria-label="Sign in"]').click()
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
                By.XPATH, Xpath.MINIMIZE_MESSAGES))).click()
        except:
            pass
