class Cart:
    def __init__(self, page):
        self.page = page

    @property
    def checkout_button(self):
        return self.page.locator('a#cart_checkout1')

    @property
    def update_button(self):
        return self.page.locator('button#cart_update')

    @property
    def empty_cart_div(self):
        return self.page.locator('div.contentpanel:has-text("Your shopping cart is empty!")')

    @property
    def confirm_order_button(self):
        return self.page.locator('button#checkout_btn')

    @property
    def processed_order_heading(self):
        return self.page.locator('h1.heading1 span.maintext:has-text("Your Order Has Been Processed!")')

    def click_checkout(self):
        self.checkout_button.wait_for(state='visible')
        self.checkout_button.click()

    def cart_is_empty(self):
        self.empty_cart_div.wait_for(state='visible')
        return self.empty_cart_div.is_visible()

    def click_confirm_order_button(self):
        self.confirm_order_button.wait_for(state='visible')
        self.confirm_order_button.click()

    def is_order_processed(self):
        self.processed_order_heading.wait_for(state='visible')
        return self.processed_order_heading.is_visible()