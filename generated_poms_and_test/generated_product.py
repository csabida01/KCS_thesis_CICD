from playwright.sync_api import Page, expect

class Product:
    def __init__(self, page: Page):
        self.page = page

    def search_for_product(self, text):
        self.page.wait_for_selector('#filter_keyword')
        self.page.fill('#filter_keyword', text)
        self.page.press('#filter_keyword', 'Enter')

    def click_result_by_title(self, title_text):
        selector = f'a[title="{title_text}"]'
        self.page.wait_for_selector(selector)
        self.page.locator(selector).click()

    def add_current_product_to_cart(self):
        # lipstick datasheet "Add to cart" button is <a class="cart">
        self.page.wait_for_selector('a.cart')
        self.page.locator('a.cart').click()

    def add_lip_search_grid_product_to_cart(self, data_id):
        self.page.wait_for_selector(f'a.productcart[data-id="{data_id}"]')
        self.page.locator(f'a.productcart[data-id="{data_id}"]').click()

    def is_no_search_results_message_visible(self):
        self.page.wait_for_selector('div.contentpanel > div', timeout=8000)
        return self.page.inner_text('div.contentpanel > div').strip() == "There is no product that matches the search criteria."

    def get_no_search_results_text(self):
        self.page.wait_for_selector('div.contentpanel > div', timeout=8000)
        return self.page.inner_text('div.contentpanel > div').strip()