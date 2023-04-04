import sys
sys.path.append('.')
import pytest
from utils.pages_url import login_page, home_page
from playwright.sync_api import expect

@pytest.fixture
def set_up(page):
    page.goto(login_page)
   
    user_login = page.locator("[data-test='username']")
    user_login.click()
    user_login.fill("standard_user")
 
    user_pass = page.locator("[data-test='password']")
    user_pass.click()
    user_pass.fill("secret_sauce")
    
    login_button = page.locator("[data-test='login-button']")
    login_button.click()      
    expect(page).to_have_url(home_page)

    yield page

    page.close()