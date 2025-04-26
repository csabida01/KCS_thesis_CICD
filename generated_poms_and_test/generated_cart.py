class Cart:
    def __init__(self, page):
        self.page = page

    # FROM HEADER: click 'Checkout'
    def goto_checkout_header(self):
        self.page.wait_for_selector('a.menu_checkout')
        self.page.click('a.menu_checkout')

    # CHECKOUT PAGE
    def is_checkout_available(self):
        self.page.wait_for_selector('a#cart_checkout1')
        return self.page.is_visible('a#cart_checkout1')

    # CHECKOUT PAGE: Confirm Order
    def click_confirm_order(self):
        self.page.wait_for_selector('button#checkout_btn')
        self.page.click('button#checkout_btn')

    # CHECKOUT PAGE: Update cart
    def click_update(self):
        self.page.wait_for_selector('button#cart_update')
        self.page.click('button#cart_update')

    # EMPTY CART
    def is_cart_empty(self):
        self.page.wait_for_selector('h1.heading1 span.maintext')
        text = self.page.inner_text('h1.heading1 span.maintext')
        return "Shopping Cart" in text and "empty" in self.page.inner_text('div.contentpanel').lower()