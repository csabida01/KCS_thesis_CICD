from playwright.sync_api import Page


class Cart:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://automationteststore.com/")
        self.cart_button = self.page.get_by_role("link", name="Cart").first
        self.continue_button = page.get_by_role("link", name="Continue")
        self.checkout_button = self.page.locator("#cart_checkout1")
        self.confirm_order_button = self.page.get_by_role("button", name="Confirm Order")
        self.success_submenu = page.locator('a[href="https://automationteststore.com/index.php?rt=checkout/success"]')

    def view_cart_content(self):
        self.cart_button.click()

    def is_cart_empty(self):
        return self.checkout_button.is_hidden()

    def buy_products(self):
        if self.is_cart_empty():
            self.continue_button.click()
        else:
            self.checkout_button.click()
            self.confirm_order_button.click()

    def is_purchase_successful(self):
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_url("https://automationteststore.com/index.php?rt=checkout/success", timeout=90000)
        if "success" in self.page.url:
            return True
        else:
            return False
