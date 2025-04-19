class Cart:
    def __init__(self, page):
        self.page = page

    # Checkout button in cart
    def get_checkout_button(self):
        return self.page.locator('a#cart_checkout1[title="Checkout"]')

    def get_update_button(self):
        return self.page.locator('button#cart_update[title="Update"]')

    # Confirm Order
    def get_confirm_order_button(self):
        return self.page.locator('button#checkout_btn[title="Confirm Order"]')

    # "Order Success" - detect after order is processed, heading1 with fa-thumbs-up
    def get_success_heading(self):
        return self.page.locator('h1.heading1 .fa-thumbs-up')

    # Empty Cart detection (uses fa-frown)
    def get_empty_cart_heading(self):
        return self.page.locator('h1.heading1 .fa-frown')

    # "Continue" button after success or empty cart
    def get_continue_button(self):
        return self.page.locator('a.btn[title="Continue"]')