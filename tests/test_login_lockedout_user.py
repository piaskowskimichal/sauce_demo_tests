import sys
sys.path.append('.')
from models.login_lockedout_user import LoginLockedOutUser
from playwright.sync_api import Page

def test_login_locked_out_user(page: Page):

    test_login_lockedout=LoginLockedOutUser(page)
    test_login_lockedout.navigate()
    test_login_lockedout.user_login()
    test_login_lockedout.user_password()
    test_login_lockedout.login_button()
    test_login_lockedout.check_login()