import sys
sys.path.append('.')
from models.login import Login
from playwright.sync_api import Playwright,Page

def test_login(page: Page):
    
    test_login=Login(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_pass()
    test_login.login_button()
    test_login.login_ok()
