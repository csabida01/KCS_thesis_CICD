class Cart:
    def __init__(self, page):
        self.page = page

    def click_checkout(self):
        # Checkout in the cart page's top right orange button
        self.page.locator('a#cart_checkout1.btn.btn-orange[title="Checkout"]').wait_for(state="visible", timeout=10000)
        self.page.locator('a#cart_checkout1.btn.btn-orange[title="Checkout"]').click()

    def click_update(self):
        self.page.locator('button#cart_update.btn.btn-default[title="Update"]').wait_for(state="visible", timeout=10000)
        self.page.locator('button#cart_update.btn.btn-default[title="Update"]').click()

    def is_my_account_visible(self):
        # <h2 class="heading2"><span>My Account</span></h2>
        self.page.locator('h2.heading2 span').wait_for(state="visible", timeout=10000)
        return self.page.inner_text('h2.heading2 span') == "My Account"

    def checkout_confirm_order(self):
        # Button on final checkout page
        self.page.locator('button#checkout_btn.btn.btn-orange[title="Confirm Order"]').wait_for(state="visible", timeout=10000)
        self.page.locator('button#checkout_btn.btn.btn-orange[title="Confirm Order"]').click()

    def is_cart_empty(self):
        # "Your shopping cart is empty!" text
        self.page.locator('div.contentpanel').wait_for(state="visible", timeout=10000)
        return "Your shopping cart is empty!" in self.page.inner_text('div.contentpanel')

    def is_checkout_button_appears(self):
        # on cart page, check if checkout button exists
        self.page.locator('a#cart_checkout1.btn.btn-orange[title="Checkout"]').wait_for(state="visible", timeout=10000)
        return self.page.is_visible('a#cart_checkout1.btn.btn-orange[title="Checkout"]')

    def order_processed_successfully(self):
        # <span class="maintext"><i class="fa fa-thumbs-up"></i> Your Order Has Been Processed!</span>
        self.page.locator('span.maintext').wait_for(state="visible", timeout=10000)
        return "Your Order Has Been Processed!" in self.page.inner_text('span.maintext')