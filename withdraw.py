from utilities import *
from linkedinlogin import LinkedInLogin


class LinkedInWithdraw(LinkedInLogin):
    def __init__(self):
        super().__init__()

    def nav(self):
        self.login_linkedin()
        time.sleep(1)
        self.driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
        time.sleep(3)


# TODO: withdraw invitations according to period time

