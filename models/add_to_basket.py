from playwright.sync_api import expect
    
class AddToBasket:
    def __init__(self,page):
        self.page=page

    def add_first_product(self):
        add_first_product = self.page.locator("button:has-text('Add to cart')").first
        add_first_product.click()

    def add_second_product(self):
        add_second_product = self.page.locator("button:has-text('Add to cart')").nth(1)
        add_second_product.click()

    def check_basket(self):
        check_basket= self.page.locator("a:has-text('2')")
        check_basket.click()

    def basket_ok(self):
        basket_ok = self.page.locator("a:has-text('2')")
        expect(basket_ok).to_have_text("2")