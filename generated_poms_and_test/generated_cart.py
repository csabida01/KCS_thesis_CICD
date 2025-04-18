class Cart:
    MY_ACCOUNT_HEADING2_SELECTOR = 'h2.heading2:has-text("My Account")'
    CHECKOUT_BUTTON_SELECTOR = 'a#cart_checkout1'
    UPDATE_BUTTON_SELECTOR = 'button#cart_update'
    CONFIRM_ORDER_BUTTON_SELECTOR = 'button#checkout_btn'
    ORDER_SUCCESS_SELECTOR = 'h1.heading1 span.maintext:has-text("Your Order Has Been Processed!")'
    CONTINUE_IN_CART_SELECTOR = 'div.col-md-12.col-xs-12.mt20 h1.heading1 span.maintext:has-text("Shopping Cart")'
    CART_EMPTY_MESSAGE = 'div.contentpanel:has-text("Your shopping cart is empty!")'

    def __init__(self, page):
        self.page = page

    def is_my_account_page_visible(self):
        try:
            self.page.wait_for_selector(self.MY_ACCOUNT_HEADING2_SELECTOR, timeout=10000)
            return True
        except Exception:
            return False

    def is_checkout_button_visible(self):
        try:
            self.page.wait_for_selector(self.CHECKOUT_BUTTON_SELECTOR, timeout=10000)
            return True
        except Exception:
            return False

    def click_checkout_button(self):
        self.page.wait_for_selector(self.CHECKOUT_BUTTON_SELECTOR, timeout=15000)
        self.page.click(self.CHECKOUT_BUTTON_SELECTOR)

    def click_confirm_order(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BUTTON_SELECTOR, timeout=15000)
        self.page.click(self.CONFIRM_ORDER_BUTTON_SELECTOR)

    def is_order_confirmed_visible(self):
        try:
            self.page.wait_for_selector(self.ORDER_SUCCESS_SELECTOR, timeout=10000)
            return True
        except Exception:
            return False

    def is_cart_empty_message_visible(self):
        try:
            self.page.wait_for_selector(self.CART_EMPTY_MESSAGE, timeout=10000)
            return True
        except Exception:
            return False