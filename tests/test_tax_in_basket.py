import sys
sys.path.append('.')
from models.tax_in_basket import TaxInBasket
from playwright.sync_api import Playwright,Page

def test_tax_in_basket(set_up):

    page = set_up

    test_tax_in_basket = TaxInBasket(page)
    test_tax_in_basket.add_first_product()   
    test_tax_in_basket.check_basket()
    test_tax_in_basket.go_to_checkout()
    test_tax_in_basket.enter_first_name()
    test_tax_in_basket.enter_last_name()
    test_tax_in_basket.enter_post_code()
    test_tax_in_basket.go_to_continue()
    test_tax_in_basket.check_tax_value()