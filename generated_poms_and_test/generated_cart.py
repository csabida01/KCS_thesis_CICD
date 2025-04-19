class Cart:
    def __init__(self, page):
        self.page = page
        # top header checkout
        self.checkout_link = 'a.menu_checkout'
        # cart page selectors
        self.checkout_button = 'a#cart_checkout1'
        self.update_button = 'button#cart_update'
        self.empty_cart_message = 'h1.heading1 span.maintext:has-text("Shopping Cart")'
        self.empty_cart_indicator = "div.contentpanel:has-text('Your shopping cart is empty!')"
        # confirm button
        self.confirm_order_btn = 'button#checkout_btn'
        # order processed page
        self.order_processed_heading = 'h1.heading1 span.maintext:has-text("Your Order Has Been Processed!")'
        self.success_url = 'https://automationteststore.com/index.php?rt=checkout/success'
        self.cart_url = 'https://automationteststore.com/index.php?rt=checkout/cart'

    def goto_checkout(self):
        self.page.wait_for_selector(self.checkout_link, timeout=10000)
        self.page.click(self.checkout_link)

    def is_checkout_btn_visible(self):
        self.page.wait_for_selector(self.checkout_button, timeout=10000)
        return self.page.is_visible(self.checkout_button)

    def is_cart_empty_message_visible(self):
        return self.page.is_visible(self.empty_cart_indicator)

    def click_confirm_order(self):
        self.page.wait_for_selector(self.confirm_order_btn, timeout=15000)
        self.page.click(self.confirm_order_btn)

    def current_url(self):
        return self.page.url

    def wait_for_confirm_order_btn(self):
        self.page.wait_for_selector(self.confirm_order_btn, timeout=15000)

    def wait_for_checkout_information(self):
        self.page.wait_for_selector(self.checkout_button, timeout=15000)