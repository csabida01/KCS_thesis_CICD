class Cart:
    def __init__(self, page):
        self.page = page
        self.menu_checkout = 'a.menu_checkout'
        self.confirm_order_btn = 'button#checkout_btn'
        self.checkout_button = 'a#cart_checkout1'
        self.update_button = 'button#cart_update'
        self.empty_cart_main_header = 'span.maintext:has-text("Shopping Cart")'
        self.empty_cart_content = 'div.contentpanel >> text=Your shopping cart is empty!'

    def go_to_checkout(self):
        self.page.wait_for_selector(self.menu_checkout)
        self.page.click(self.menu_checkout)

    def wait_for_checkout_button(self):
        self.page.wait_for_selector(self.checkout_button)
        return self.page.is_visible(self.checkout_button)

    def wait_for_confirm_order_button(self):
        self.page.wait_for_selector(self.confirm_order_btn)
        return self.page.is_visible(self.confirm_order_btn)

    def click_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn)
        self.page.click(self.confirm_order_btn)

    def cart_is_empty(self):
        self.page.wait_for_selector(self.empty_cart_main_header)
        return self.page.is_visible(self.empty_cart_content)