class TaxInBasket:
    def __init__(self,page):
        self.page=page

    def add_first_product(self):
        add_first_product = self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        add_first_product.click()

    def check_basket(self):
        check_basket = self.page.locator("a:has-text('1')")
        check_basket.click()
    
    def go_to_checkout(self):
        go_to_checkout = self.page.locator("[data-test='checkout']")
        go_to_checkout.click()

    def enter_first_name(self):
        enter_first_name =self.page.locator("[data-test='firstName']")
        enter_first_name.fill("Mr. Test")
        
    def enter_last_name(self):
        enter_last_name = self.page.locator("[data-test='lastName']")
        enter_last_name.fill("Testovsky")
        
    def enter_post_code(self):
        enter_post_code = self.page.locator("[data-test='postalCode']")
        enter_post_code.fill("333")

    def go_to_continue(self):
        go_to_continue = self.page.locator("[data-test='continue']")
        go_to_continue.click()


    def check_tax_value(self):
               
        expected_price = 32.39     
        price_of_item = self.page.locator('text=$29.99 >> nth=0').text_content()
        price_of_item = float(price_of_item.strip('$'))

        total_price = self.page.locator('text=$32.39 >> nth=0').text_content()
        total_price = float(total_price.strip('Total: $'))
    
        tax = 0.08
        sum = price_of_item + (tax * price_of_item)
        sum = round(sum, 2)


        if sum == 32.39:
            print ("Tax= 8%. TAX CORRECT")
        else: 
            print('Tax is NOT CORRECT!')

        assert sum == expected_price