class Cart:
    def __init__(self, page):
        self.page = page
        # Topbar Checkout button (first of the menu_checkout)
        self.checkout_header_link = 'a.menu_checkout'
        # Confirm order
        self.confirm_order_btn = 'button#checkout_btn'
        # Cart page
        self.cart_checkout_btn = 'a#cart_checkout1'
        self.cart_update_btn = 'button#cart_update'
        # "Empty cart" indication
        self.empty_cart_header = 'h1.heading1 > span.maintext'
        # "Order processed" page
        self.order_processed_header = 'h1.heading1 span.maintext'

    def go_to_cart_via_header_checkout(self):
        self.page.wait_for_selector(self.checkout_header_link, timeout=10000)
        self.page.click(self.checkout_header_link)

    def is_checkout_button_visible(self):
        # Only check visibility, don't click
        try:
            self.page.wait_for_selector(self.cart_checkout_btn, timeout=5000)
            return self.page.is_visible(self.cart_checkout_btn)
        except:
            return False

    def click_checkout_button(self):
        self.page.wait_for_selector(self.cart_checkout_btn, timeout=10000)
        self.page.click(self.cart_checkout_btn)

    def confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn, timeout=15000)
        self.page.click(self.confirm_order_btn)

    def is_empty_cart(self):
        self.page.wait_for_selector(self.empty_cart_header, timeout=10000)
        msg = self.page.inner_text(self.empty_cart_header)
        return 'Shopping Cart' in msg and self.page.content().find('Your shopping cart is empty!') != -1

    def is_order_processed(self):
        self.page.wait_for_selector(self.order_processed_header, timeout=10000)
        txt = self.page.inner_text(self.order_processed_header)
        return 'Your Order Has Been Processed!' in txt