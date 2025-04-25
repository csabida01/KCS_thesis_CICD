class Cart:
    def __init__(self, page):
        self.page = page

    # Checkout button (pull-right panel)
    def is_checkout_button_visible(self):
        return self.page.is_visible('a#cart_checkout1')

    def click_checkout_button(self):
        self.page.wait_for_selector('a#cart_checkout1', timeout=10000)
        self.page.click('a#cart_checkout1')

    # Confirm order page
    def is_confirm_order_button_visible(self):
        return self.page.is_visible('button#checkout_btn')

    def click_confirm_order_button(self):
        self.page.wait_for_selector('button#checkout_btn', timeout=10000)
        self.page.click('button#checkout_btn')

    # Cart empty message
    def is_cart_empty_message_visible(self):
        # Looks for Shopping Cart header + the text 'Your shopping cart is empty!'
        return self.page.is_visible('h1.heading1 span.maintext >> text="Shopping Cart"') and self.page.is_visible('div.contentpanel >> text="Your shopping cart is empty!"')