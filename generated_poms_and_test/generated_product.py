# generated_product.py
from playwright.sync_api import Page, expect

class Product:
    ADD_TO_CART_ON_DATASHEET = 'ul.productpagecart a.cart'
    VIVA_GLAM_LIPSTICK_LINK = 'a[title="Viva Glam Lipstick"]'
    NO_RESULT_DIV = '//div[contains(text(), "There is no product that matches the search criteria.")]'

    def __init__(self, page: Page):
        self.page = page

    def click_add_to_cart_on_datasheet(self):
        self.page.wait_for_selector(self.ADD_TO_CART_ON_DATASHEET, timeout=10000)
        self.page.locator(self.ADD_TO_CART_ON_DATASHEET).click()

    def click_viva_glam_lipstick_in_results(self):
        self.page.wait_for_selector(self.VIVA_GLAM_LIPSTICK_LINK, timeout=10000)
        self.page.locator(self.VIVA_GLAM_LIPSTICK_LINK).click()

    def no_results_div_visible(self):
        return self.page.is_visible(self.NO_RESULT_DIV)