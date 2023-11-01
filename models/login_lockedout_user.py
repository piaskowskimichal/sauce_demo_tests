import os
import sys
sys.path.append('.')
from utils.pages_url import login_page
from playwright.sync_api import expect

locked_user= os.environ.get("LOCKED_USER")
locked_user_pass= os.environ.get("LOCKED_USER_PASS")

class LoginLockedOutUser:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test=\"username\"]")
        user_login.click()
        user_login.fill(locked_user)

    def user_password(self):
        user_password = self.page.locator("[data-test=\"password\"]")
        user_password.click()
        user_password.fill(locked_user_pass)

    def login_button(self):
        login_button = self.page.locator("[data-test=\"login-button\"]")
        login_button.click()    

    def check_login(self):
        error_button= self.page.locator("[data-test='error']")
        expect(error_button).to_be_visible()