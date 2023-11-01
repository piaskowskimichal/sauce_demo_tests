import sys
sys.path.append('.')
from models.login_problem_user import LoginProblemUser
from playwright.sync_api import Page

def test_login_problem_user(page: Page):

    test_login=LoginProblemUser(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_password()
    test_login.login_button()
    test_login.check_images()
    test_login.open_menu()
    test_login.log_out()