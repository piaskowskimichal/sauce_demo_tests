import sys
sys.path.append('.')
from models.login_logout_standard_user import LoginLogoutStandardUser
from playwright.sync_api import Page

def test_login_standard_user(page: Page):
    
    test_standard_user_login=LoginLogoutStandardUser(page)
    test_standard_user_login.navigate()
    test_standard_user_login.user_login()
    test_standard_user_login.user_password()
    test_standard_user_login.login_button()
    test_standard_user_login.check_login()
    test_standard_user_login.open_menu()
    test_standard_user_login.log_out()