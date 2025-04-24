class Product:
    def __init__(self, page):
        self.page = page

    # Lipstick datasheet page
    ADD_TO_CART_LINK = "ul.productpagecart a.cart"
    QTY_INPUT = "input#product_quantity"
    COLOR_DROPDOWN = "select#option305"

    # Search results (grid)
    # For the "Viva Glam Lipstick"
    VIVA_GLAM_LIPSTICK_LINK = "a[title='Viva Glam Lipstick']"
    VIVA_GLAM_LIPSTICK_ADD_TO_CART = "a.productcart[data-id='59']"

    # For empty results
    EMPTY_RESULT_ALERT = "div.contentpanel > div:has-text('There is no product that matches the search criteria.')"

    def add_current_to_cart(self, qty=None, color=None):
        if qty is not None:
            self.page.wait_for_selector(self.QTY_INPUT)
            self.page.fill(self.QTY_INPUT, str(qty))
        if color is not None:
            self.page.wait_for_selector(self.COLOR_DROPDOWN)
            self.page.select_option(self.COLOR_DROPDOWN, color)
        self.page.wait_for_selector(self.ADD_TO_CART_LINK)
        self.page.click(self.ADD_TO_CART_LINK)

    def select_viva_glam_lipstick_from_search(self):
        self.page.wait_for_selector(self.VIVA_GLAM_LIPSTICK_LINK)
        self.page.click(self.VIVA_GLAM_LIPSTICK_LINK)

    def add_viva_glam_lipstick_to_cart_from_search(self):
        self.page.wait_for_selector(self.VIVA_GLAM_LIPSTICK_ADD_TO_CART)
        self.page.click(self.VIVA_GLAM_LIPSTICK_ADD_TO_CART)

    def is_empty_results_alert_visible(self):
        self.page.wait_for_selector("div.contentpanel")
        return "There is no product that matches the search criteria." in self.page.locator("div.contentpanel").inner_text()