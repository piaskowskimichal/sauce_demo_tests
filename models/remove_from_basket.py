from playwright.sync_api import expect

class RemoveFromBasket:
    def __init__(self,page):
        self.page=page

    def add_first_product(self):
        add_first_product = self.page.locator("button:has-text('Add to cart')").first
        add_first_product.click()

    def add_second_product(self):
        add_second_product = self.page.locator("button:has-text('Add to cart')").nth(1)
        add_second_product.click()

    def basket_checkout(self):
        basket_checkout = self.page.locator("a:has-text('2')")
        basket_checkout.click()

    def remove_product(self):
        remove_product =  self.page.locator("button:has-text('Remove')").first
        remove_product.click()

    def basket_ok(self):
        basket_ok = self.page.locator("a:has-text('1')")   
        expect(basket_ok).to_have_text("1")        