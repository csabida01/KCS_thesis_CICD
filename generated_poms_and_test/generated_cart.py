class Cart:
    def __init__(self, page):
        self.page = page

    def checkout_button(self):
        return self.page.locator('a#cart_checkout1')

    def update_button(self):
        return self.page.locator('button#cart_update')

    def confirm_order_button(self):
        return self.page.locator('button#checkout_btn')

    def order_processed_heading(self):
        return self.page.locator('span.maintext:has-text("Your Order Has Been Processed!")')

    def empty_cart_msg(self):
        return self.page.locator('div.contentpanel:has-text("Your shopping cart is empty!")')

    def continue_button(self):
        # after order or empty cart
        return self.page.locator('a.btn.btn-default[title="Continue"]')

    # Util method to go to cart (by menu or direct URL)
    def go_to_checkout(self):
        # Use first element in menu
        self.page.locator('a.menu_checkout').first.click()