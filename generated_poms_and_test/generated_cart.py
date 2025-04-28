from playwright.sync_api import Page, expect

class Cart:
    def __init__(self, page: Page):
        self.page = page

    def is_checkout_visible(self):
        self.page.wait_for_selector('#cart_checkout1', timeout=10000)
        return self.page.is_visible('#cart_checkout1')

    def click_checkout(self):
        self.page.wait_for_selector('#cart_checkout1', timeout=10000)
        self.page.locator('#cart_checkout1').click()

    def click_confirm_order(self):
        # on confirm order page
        self.page.wait_for_selector('button#checkout_btn', timeout=12000)
        self.page.locator('button#checkout_btn').click()

    def order_success_message_visible(self):
        self.page.wait_for_selector('span.maintext', timeout=8000)
        maintext = self.page.inner_text('span.maintext')
        return "Your Order Has Been Processed" in maintext

    def is_cart_empty(self):
        # After pressing checkout, if cart is empty, this appears:
        self.page.wait_for_selector('span.maintext', timeout=10000)
        return self.page.inner_text('span.maintext').strip() == "Shopping Cart"