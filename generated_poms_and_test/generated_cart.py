class Cart:
    def __init__(self, page):
        self.page = page
        # Checkout button (Update and checkout)
        self.checkout_button = "a#cart_checkout1"
        # Update cart button
        self.update_button = "button#cart_update"
        # Confirm order button (Confirm order)
        self.confirm_order_btn = "button#checkout_btn"
        # Empty cart indicator ("Your shopping cart is empty!")
        self.empty_cart_h1 = "h1.heading1 span.maintext:has-text('Shopping Cart')"
        self.empty_cart_content = "div.contentpanel:has-text('Your shopping cart is empty!')"
        # Success order processed h1
        self.success_heading = "h1.heading1 span.maintext:has-text('Your Order Has Been Processed!')"

    def can_see_checkout_btn(self):
        self.page.wait_for_selector(self.checkout_button, timeout=12000)
        return self.page.is_visible(self.checkout_button)

    def click_checkout(self):
        self.page.wait_for_selector(self.checkout_button, timeout=12000)
        self.page.click(self.checkout_button)

    def wait_for_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn, timeout=15000)
        return self.page.is_visible(self.confirm_order_btn)

    def click_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn, timeout=15000)
        self.page.click(self.confirm_order_btn)

    def cart_is_empty(self):
        self.page.wait_for_selector(self.empty_cart_content, timeout=8000)
        return self.page.is_visible(self.empty_cart_content)

    def order_success_heading(self):
        self.page.wait_for_selector(self.success_heading, timeout=12000)
        return self.page.is_visible(self.success_heading)