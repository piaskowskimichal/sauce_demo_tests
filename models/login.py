import sys
sys.path.append('.')
from utils.pages_url import login_page, home_page
from playwright.sync_api import Playwright, sync_playwright, expect

class Login:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test='username']")
        user_login.click()
        user_login.fill("standard_user")

    def user_password(self):
        user_password = self.page.locator("[data-test='password']")
        user_password.click()
        user_password.fill("secret_sauce")

    def login_button(self):
        login_button = self.page.locator("[data-test='login-button']")
        login_button.click()
        expect(self.page).to_have_url(home_page)    

    def check_login(self):
        product_tab = self.page.locator("text=Products")  
        expect(product_tab).to_have_text("Products")