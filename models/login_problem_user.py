import os
import sys
sys.path.append('.')
from utils.pages_url import login_page
from playwright.sync_api import expect

problem_user= os.environ.get("PROBLEM_USER")
problem_user_pass= os.environ.get("PROBLEM_USER_PASS")

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

    def check_images(self):
        img_first = self.page.locator("div.inventory_item_img > a > img").first
        expect(img_first).to_have_attribute("src", "/static/media/sl-404.168b1cce.jpg")
        img_last = self.page.locator("div.inventory_item_img > a > img").last
        expect(img_last).to_have_attribute("src", "/static/media/sl-404.168b1cce.jpg")
    
    def open_menu(self):
        open_menu = self.page.locator("text=Open Menu")
        open_menu.click()

    def log_out(self):
        log_out = self.page.locator("text=Logout")
        log_out.click()
