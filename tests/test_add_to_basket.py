import sys
sys.path.append('.')
from models.add_to_basket import AddToBasket


def test_add_to_basket(set_up):

    page = set_up
   
    test_add_to_basket = AddToBasket(page)
    test_add_to_basket.add_first_product()
    test_add_to_basket.add_second_product()
    test_add_to_basket.check_basket()
    test_add_to_basket.basket_ok()