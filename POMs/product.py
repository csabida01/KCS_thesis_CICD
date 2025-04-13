from playwright.sync_api import Page


class Product:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://automationteststore.com/")
        self.search_bar = self.page.get_by_placeholder("Search Keywords")
        self.search_button = self.page.locator("div.button-in-search")
        self.product_list = self.page.locator("i.fa-cart-plus").first
        self.sort_dropdown = self.page.locator("#sort").first
        self.add_to_cart_button = self.page.get_by_role("link", name="Add to Cart")
        self.checkout_button = self.page.locator("#cart_checkout1")

    def product_search(self, item_name):
        self.search_bar.fill(item_name)
        self.search_button.click()
        if self.sort_dropdown.is_visible():
            self.product_list.click()

    def add_product_to_cart(self):
        self.page.wait_for_timeout(100)
        if self.add_to_cart_button.is_visible():
            self.add_to_cart_button.click()

    def is_product_added(self):
        return self.checkout_button.is_visible()
