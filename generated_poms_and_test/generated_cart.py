# generated_cart.py
from playwright.sync_api import Page, expect

class Cart:
    MY_ACCOUNT_HEADING = ".sidewidt .heading2"
    CHECKOUT_BUTTON_IN_CART = "#cart_checkout1"
    CONFIRM_ORDER_BUTTON = "#checkout_btn"
    EMPTY_CART_HEADER = 'span.maintext' # contains "Shopping Cart"

    def __init__(self, page: Page):
        self.page = page

    def my_account_heading_is_visible(self):
        self.page.wait_for_selector(self.MY_ACCOUNT_HEADING, timeout=10000)
        return self.page.is_visible(self.MY_ACCOUNT_HEADING)

    def checkout_button_visible(self):
        self.page.wait_for_selector(self.CHECKOUT_BUTTON_IN_CART, timeout=10000)
        return self.page.is_visible(self.CHECKOUT_BUTTON_IN_CART)

    def click_checkout_button(self):
        self.page.wait_for_selector(self.CHECKOUT_BUTTON_IN_CART, timeout=10000)
        self.page.locator(self.CHECKOUT_BUTTON_IN_CART).click()

    def confirm_order_button_visible(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BUTTON, timeout=20000)
        return self.page.is_visible(self.CONFIRM_ORDER_BUTTON)
    
    def click_confirm_order_button(self):
        self.page.wait_for_selector(self.CONFIRM_ORDER_BUTTON, timeout=20000)
        self.page.locator(self.CONFIRM_ORDER_BUTTON).click()

    def empty_cart_visible(self):
        self.page.wait_for_selector(self.EMPTY_CART_HEADER, timeout=10000)
        return self.page.inner_text(self.EMPTY_CART_HEADER).strip() == "Shopping Cart"