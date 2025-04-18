class Product:
    SEARCH_INPUT_SELECTOR = 'input#filter_keyword'
    SEARCH_BUTTON_SELECTOR = 'div.button-in-search'
    ENTER_KEY = 'Enter'
    ADD_TO_CART_BUTTON_GRID = 'a.productcart[data-id="59"]'
    ADD_TO_CART_BUTTON_DATASHEET = 'ul.productpagecart > li > a.cart'
    GRID_VIVA_GLAM_LIPSTICK_LINK = 'a[title="Viva Glam Lipstick"]'
    NO_RESULTS_DIV = 'div.contentpanel > div:has-text("There is no product that matches the search criteria.")'

    def __init__(self, page):
        self.page = page

    def search_for_product(self, keyword):
        self.page.wait_for_selector(self.SEARCH_INPUT_SELECTOR, timeout=15000)
        self.page.click(self.SEARCH_INPUT_SELECTOR)
        self.page.fill(self.SEARCH_INPUT_SELECTOR, keyword)
        self.page.keyboard.press(self.ENTER_KEY)

    def click_add_to_cart_from_grid_viva_glam_lipstick(self):
        self.page.wait_for_selector(self.GRID_VIVA_GLAM_LIPSTICK_LINK, timeout=15000)
        self.page.click(self.GRID_VIVA_GLAM_LIPSTICK_LINK)
        self.page.wait_for_selector(self.ADD_TO_CART_BUTTON_DATASHEET, timeout=15000)
        self.page.click(self.ADD_TO_CART_BUTTON_DATASHEET)

    def click_add_to_cart_from_datasheet(self):
        self.page.wait_for_selector(self.ADD_TO_CART_BUTTON_DATASHEET, timeout=15000)
        self.page.click(self.ADD_TO_CART_BUTTON_DATASHEET)

    def is_no_product_found_message_visible(self):
        try:
            self.page.wait_for_selector(self.NO_RESULTS_DIV, timeout=10000)
            return True
        except Exception:
            return False