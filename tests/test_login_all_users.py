import sys
sys.path.append('.')
from models.login_all_users import LoginStandardUser, LoginLockedOutUser, LoginProblemUser, LoginPerformaceGlitchUser
from playwright.sync_api import Page

def test_login_standard_user(page: Page):
    
    test_login=LoginStandardUser(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_password()
    test_login.login_button()
    test_login.check_login()
    test_login.open_menu()
    test_login.log_out()

def test_login_locked_out_user(page: Page):

    test_login=LoginLockedOutUser(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_password()
    test_login.login_button()
    test_login.check_login()
    test_login.open_menu()
    test_login.log_out()

def test_login_problem_user(page: Page):

    test_login=LoginProblemUser(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_password()
    test_login.login_button()
    test_login.check_login()
    test_login.open_menu()
    test_login.log_out()

def test_login_performace_glitch_user(page: Page):
    test_login=LoginPerformaceGlitchUser(page)
    test_login.navigate()
    test_login.user_login()
    test_login.user_password()
    test_login.login_button()
    test_login.check_login()
    test_login.open_menu()
    test_login.log_out()