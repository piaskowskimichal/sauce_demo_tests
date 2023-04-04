import sys
sys.path.append('.')
from models.remove_from_basket import RemoveFromBasket
from playwright.sync_api import Playwright,Page

def test_remove_from_basket(set_up):

    page = set_up

    test_remove_from_basket = RemoveFromBasket(page)
    test_remove_from_basket.add_first_product()
    test_remove_from_basket.add_second_product()
    test_remove_from_basket.basket_checkout()
    test_remove_from_basket.remove_product()
    test_remove_from_basket.basket_ok()