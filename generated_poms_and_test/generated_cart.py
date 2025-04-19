class Cart:
    def __init__(self, page):
        self.page = page

    # Cart page - checkout button
    def checkout_button(self):
        return self.page.locator('a#cart_checkout1')

    # Cart page - update button
    def update_button(self):
        return self.page.locator('button#cart_update')

    # Confirm page - confirm order button
    def confirm_order_btn(self):
        return self.page.locator('button#checkout_btn')

    # Empty cart message
    def empty_cart_message(self):
        return self.page.locator('h1.heading1 span.maintext', has_text="Shopping Cart")

    # Continue button (after order processed or empty cart)
    def continue_button(self):
        return self.page.locator('a.btn.btn-default.mr10[title="Continue"]')

    # Order processed heading
    def order_processed_heading(self):
        return self.page.locator('h1.heading1 span.maintext', has_text="Your Order Has Been Processed!")