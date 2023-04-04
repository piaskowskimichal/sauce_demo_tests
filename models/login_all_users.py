import sys
sys.path.append('.')
from utils.pages_url import login_page, home_page
from playwright.sync_api import Playwright, sync_playwright, expect

class LoginStandardUser:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test=\"username\"]")
        user_login.click()
        user_login.fill("standard_user")

    def user_password(self):
        user_password = self.page.locator("[data-test=\"password\"]")
        user_password.click()
        user_password.fill("secret_sauce")

    def login_button(self):
        login_button = self.page.locator("[data-test=\"login-button\"]")
        login_button.click()    

    def check_login(self):
        expect(self.page).to_have_url(home_page)
        product_tab = self.page.locator("text=Products")  
        expect(product_tab).to_have_text("Products")

    def open_menu(self):
        open_menu = self.page.locator("text=Open Menu")
        open_menu.click()

    def log_out(self):
        log_out = self.page.locator("text=Logout")
        log_out.click()

class LoginLockedOutUser:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test=\"username\"]")
        user_login.click()
        user_login.fill("locked_out_user")

    def user_password(self):
        user_password = self.page.locator("[data-test=\"password\"]")
        user_password.click()
        user_password.fill("secret_sauce")

    def login_button(self):
        login_button = self.page.locator("[data-test=\"login-button\"]")
        login_button.click()    

    def check_login(self):
        expect(self.page).to_have_url(home_page)
        product_tab = self.page.locator("text=Products")  
        expect(product_tab).to_have_text("Products")

    def open_menu(self):
        open_menu = self.page.locator("text=Open Menu")
        open_menu.click()

    def log_out(self):
        log_out = self.page.locator("text=Logout")
        log_out.click()

class LoginProblemUser:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test=\"username\"]")
        user_login.click()
        user_login.fill("problem_user")

    def user_password(self):
        user_password = self.page.locator("[data-test=\"password\"]")
        user_password.click()
        user_password.fill("secret_sauce")

    def login_button(self):
        login_button = self.page.locator("[data-test=\"login-button\"]")
        login_button.click()    

    def check_login(self):
        expect(self.page).to_have_url(home_page)
        product_tab = self.page.locator("text=Products")  
        expect(product_tab).to_have_text("Products")

    def open_menu(self):
        open_menu = self.page.locator("text=Open Menu")
        open_menu.click()

    def log_out(self):
        log_out = self.page.locator("text=Logout")
        log_out.click()

class LoginPerformaceGlitchUser:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(login_page)

    def user_login(self):
        user_login = self.page.locator("[data-test=\"username\"]")
        user_login.click()
        user_login.fill("performance_glitch_user")

    def user_password(self):
        user_password = self.page.locator("[data-test=\"password\"]")
        user_password.click()
        user_password.fill("secret_sauce")

    def login_button(self):
        login_button = self.page.locator("[data-test=\"login-button\"]")
        login_button.click()    

    def check_login(self):
        expect(self.page).to_have_url(home_page)
        product_tab = self.page.locator("text=Products")  
        expect(product_tab).to_have_text("Products")

    def open_menu(self):
        open_menu = self.page.locator("text=Open Menu")
        open_menu.click()

    def log_out(self):
        log_out = self.page.locator("text=Logout")
        log_out.click()